#!/usr/bin/env python3
"""
sync_progress.py
================
Automated Workflow for C Challenge Repository:
  1. Scans workspace for solved .c challenge files (verifies content & sanity).
  2. Updates `250_C_QUESTIONS.md` (ticks [X] / unticks [ ]).
  3. Updates `Spaced_Repetition_Tracker.md` (registers newly solved challenges & updates status).
  4. Updates `README.md` (live stats dashboard, progress bar, topic table).
  5. Automatically stages, generates smart commit messages, and commits changes to Git.

Usage:
  python sync_progress.py            # Sync docs & create Git commit if changes exist
  python sync_progress.py --push     # Sync, commit, and push to GitHub (origin/main)
  python sync_progress.py --no-commit # Sync docs only (do not commit to Git)
  python sync_progress.py -m "My custom commit message"
"""

import sys
import os
import re
import subprocess
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WORKSPACE = Path(__file__).parent.resolve()

TOPIC_DIRS = [
    ("01", "01_Simple_C_Questions", "1. Simple C Questions"),
    ("02", "02_If_Else_Statement", "2. If/Else Statement"),
    ("03", "03_Loops", "3. Loops"),
    ("04", "04_Switch_Case", "4. Switch Case"),
    ("05", "05_Array_Questions", "5. Array Questions"),
    ("06", "06_Matrix_Questions", "6. Matrix Questions"),
    ("07", "07_String_Questions", "7. String Questions List"),
    ("08", "08_String_Questions_Level_Up", "8. String Questions: Level Up"),
    ("09", "09_Function_Questions", "9. Function Questions"),
    ("10", "10_Pointer_Questions", "10. Pointer Questions"),
    ("11", "11_File_Handling", "11. File Handling"),
    ("12", "12_Sorting", "12. Sorting"),
    ("13", "13_Searching", "13. Searching"),
    ("14", "14_Tricky_Questions", "14. Tricky Questions for Expert Only | Legendary level"),
    ("15", "15_Puzzles_Questions", "15. Puzzles Questions"),
]

def is_valid_c_solution(filepath: Path) -> bool:
    """
    Sanity check to ensure file contains actual written code.
    Requires:
      - File size > 20 bytes
      - Contains core C syntax (e.g. main, include, return, or braces)
    """
    try:
        if filepath.stat().st_size < 20:
            return False
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        # Strip comments
        clean = re.sub(r"/\*.*?\*/", "", content, flags=re.DOTALL)
        clean = re.sub(r"//.*", "", clean)
        # Check for code tokens
        has_code = bool(re.search(r"\b(main|include|return|int|void|char|float|double|printf|scanf)\b", clean))
        has_braces = "{" in clean and "}" in clean
        return has_code and has_braces
    except Exception:
        return False

def find_c_files():
    """Find all valid, written .c solution files in topic directories."""
    c_files = {}  # filename_lower -> metadata
    for root, _, files in os.walk(WORKSPACE):
        if ".git" in root or "scratch" in root:
            continue
        for f in files:
            if f.endswith(".c"):
                full_path = Path(root) / f
                if is_valid_c_solution(full_path):
                    rel_path = full_path.relative_to(WORKSPACE)
                    parts = rel_path.parts
                    section_folder = parts[0] if len(parts) > 1 else "Root"
                    c_files[f.lower()] = {
                        "filename": f,
                        "rel_path": str(rel_path),
                        "section": section_folder,
                    }
    return c_files

def clean_problem_name(filename: str) -> str:
    """Format a filename into a clean human-readable title."""
    name = filename
    if name.endswith(".c"):
        name = name[:-2]
    name = name.replace("_", " ")
    name = re.sub(r"\s+", " ", name).strip()
    return name

def sync_250_questions(existing_c_files):
    """Update checkbox marks in 250_C_QUESTIONS.md based on valid solution files."""
    questions_file = WORKSPACE / "250_C_QUESTIONS.md"
    if not questions_file.exists():
        return 0, 0, {}

    content = questions_file.read_text(encoding="utf-8")
    lines = content.splitlines()

    new_lines = []
    current_section = None
    section_stats = {}
    total_completed = 0
    total_questions = 0

    for line in lines:
        if line.startswith("## "):
            sec_name = line[3:].strip()
            current_section = sec_name
            if current_section not in section_stats:
                section_stats[current_section] = {"total": 0, "solved": 0}
        
        m = re.match(r"^-\s*\[([ xX])\]\s+(.+\.c)\s*$", line)
        if m:
            total_questions += 1
            filename = m.group(2).strip()
            is_solved = filename.lower() in existing_c_files

            if current_section:
                section_stats[current_section]["total"] += 1
                if is_solved:
                    section_stats[current_section]["solved"] += 1

            if is_solved:
                total_completed += 1
                new_lines.append(f"- [X] {filename}")
            else:
                new_lines.append(f"- [ ] {filename}")
        else:
            new_lines.append(line)

    questions_file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    return total_completed, total_questions, section_stats

def generate_progress_bar(percentage, width=40):
    """Generate a visual text progress bar."""
    filled = int(round((percentage / 100) * width))
    unfilled = width - filled
    return "█" * filled + "░" * unfilled

def sync_readme(total_completed, total_questions, section_stats):
    """Update README.md with live metrics and topic breakdown."""
    readme_file = WORKSPACE / "README.md"
    if not readme_file.exists():
        return

    content = readme_file.read_text(encoding="utf-8")
    percentage = (total_completed / total_questions * 100) if total_questions > 0 else 0.0
    pending = total_questions - total_completed
    bar = generate_progress_bar(percentage)

    # Update Dashboard metrics
    content = re.sub(r"\*\*Total Challenges\*\*\s*\|\s*`\d+`", f"**Total Challenges** | `{total_questions}`", content)
    content = re.sub(r"\*\*Completed\*\*\s*\|\s*`\d+`", f"**Completed** | `{total_completed}`", content)
    content = re.sub(r"\*\*Pending\*\*\s*\|\s*`\d+`", f"**Pending** | `{pending}`", content)
    content = re.sub(r"\*\*Current Completion Rate\*\*\s*\|\s*`[\d\.]+%\`", f"**Current Completion Rate** | `{percentage:.2f}%`", content)
    content = re.sub(r"Progress:\s*\[[█░]+\]\s*[\d\.]+%\s*\(\d+\s*/\s*\d+\)", f"Progress: [{bar}] {percentage:.2f}% ({total_completed} / {total_questions})", content)

    # Update Topic Breakdown rows
    for num_str, folder, sec_header in TOPIC_DIRS:
        stats = None
        for k, v in section_stats.items():
            if sec_header.lower() in k.lower() or folder.lower() in k.lower():
                stats = v
                break
        if not stats:
            stats = {"total": 0, "solved": 0}

        solved = stats["solved"]
        tot = stats["total"]
        if tot > 0 and solved == tot:
            status = "✅ Completed"
        elif solved > 0:
            status = "⏳ In Progress"
        else:
            status = "⭕ Not Started"

        row_pattern = rf"\|\s*{num_str}\s*\|\s*\[`{folder}`\]\([^\)]+\)\s*\|\s*[^\|]+\|\s*\d+\s*/\s*\d+\s*\|"
        new_row = f"| {num_str} | [`{folder}`](./{folder}/) | {status} | {solved} / {tot} |"
        content = re.sub(row_pattern, new_row, content)

    readme_file.write_text(content, encoding="utf-8")

def sync_spaced_tracker(existing_c_files, section_stats):
    """Update Spaced_Repetition_Tracker.md with active problems and pending counts."""
    tracker_file = WORKSPACE / "Spaced_Repetition_Tracker.md"
    if not tracker_file.exists():
        return

    today = datetime.now().strftime("%Y-%m-%d")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    content = tracker_file.read_text(encoding="utf-8")

    # Parse existing rows in active schedule table
    existing_tracked_rows = []
    active_table_match = re.search(r"## 📂 Active Review Schedule\s*\n+(.*?)\n+---\s*\n+## ⏳ Pending Topics", content, re.DOTALL)
    
    existing_problem_names = set()
    if active_table_match:
        table_text = active_table_match.group(1)
        for line in table_text.splitlines():
            line = line.strip()
            if line.startswith("|") and not line.startswith("| Problem Name") and not line.startswith("| :---") and not "*(None yet)*" in line:
                cols = [c.strip() for c in line.split("|")[1:-1]]
                if len(cols) >= 6:
                    existing_tracked_rows.append(cols)
                    existing_problem_names.add(cols[0].lower())

    # Add any newly solved problems not yet in the active table
    for f_lower, f_info in existing_c_files.items():
        clean_name = clean_problem_name(f_info["filename"])
        if clean_name.lower() not in existing_problem_names:
            existing_tracked_rows.append([
                clean_name,
                f_info["section"],
                today,
                tomorrow,
                "1 Day",
                "Initial solution completed"
            ])
            existing_problem_names.add(clean_name.lower())

    # Reconstruct Active Review Schedule Table
    if existing_tracked_rows:
        active_table_lines = [
            "| Problem Name | Section | Last Reviewed | Next Review | Interval | Status / Notes |",
            "| :--- | :--- | :---: | :---: | :---: | :--- |"
        ]
        for row in existing_tracked_rows:
            active_table_lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} |")
        active_table_str = "\n".join(active_table_lines)
    else:
        active_table_str = (
            "*No problems completed yet. When you solve a challenge in any topic folder, add it here to begin the spaced repetition review cycle.*\n\n"
            "| Problem Name | Section | Last Reviewed | Next Review | Interval | Status / Notes |\n"
            "| :--- | :--- | :---: | :---: | :---: | :--- |\n"
            "| *(None yet)* | — | — | — | — | Solve your first problem to start! |"
        )

    # Reconstruct Pending Topics Table
    pending_table_lines = [
        "| Topic / Section | Total Problems | Solved | Status |",
        "| :--- | :---: | :---: | :--- |"
    ]
    for num_str, folder, sec_header in TOPIC_DIRS:
        stats = None
        for k, v in section_stats.items():
            if sec_header.lower() in k.lower() or folder.lower() in k.lower():
                stats = v
                break
        if not stats:
            stats = {"total": 0, "solved": 0}

        solved = stats["solved"]
        tot = stats["total"]
        if tot > 0 and solved == tot:
            status = "✅ Completed"
        elif solved > 0:
            status = "⏳ In Progress"
        else:
            status = "⭕ Not Started"

        pending_table_lines.append(f"| `{folder}` | {tot} | {solved} | {status} |")

    pending_table_str = "\n".join(pending_table_lines)

    header = (
        "# 🧠 C 250+ Challenges: Spaced Repetition Tracker\n\n"
        "**Mastery Strategy:** Hermann Ebbinghaus Forgetfulness Curve 📉  \n"
        "**Algorithm Intervals:** 1 Day → 3 Days → 7 Days → 14 Days → 30 Days → 🎓 Mastered\n\n"
        "---\n\n"
        "### 🛠️ How this works:\n"
        "1. **Daily Review:** Every session, check for problems marked **\"ASAP\"** or with today's date.\n"
        "2. **Success (Perfect Code):** Move to the next interval (e.g., 1 Day → 3 Days).\n"
        "3. **Struggle (Logical Error):** Reset to **1 Day** to rebuild muscle memory.\n"
        "4. **Mastery Path:** 1 → 3 → 7 → 14 → 30 → 🎓 **Mastered**\n\n"
        "---\n\n"
        "## 📂 Active Review Schedule\n\n"
    )

    footer = (
        "\n\n---\n\n"
        "## ⏳ Pending Topics — Not Yet Solved\n\n"
        f"{pending_table_str}\n\n"
        "---\n\n"
        "*\"Repetition is the mother of learning, the father of action, which makes it the architect of accomplishment.\"* 🧱\n"
    )

    new_tracker_content = f"{header}{active_table_str}{footer}"
    tracker_file.write_text(new_tracker_content, encoding="utf-8")

def get_git_status():
    """Check if there are unstaged or untracked changes."""
    try:
        res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=WORKSPACE)
        return res.stdout.strip()
    except Exception as e:
        print(f"⚠️ Git status check failed: {e}")
        return ""

def git_commit_and_push(custom_message=None, push=False, completed=0, total=0):
    """Automatically git add, git commit, and optionally git push."""
    status = get_git_status()
    if not status:
        print("Git working tree is clean. Nothing to commit.")
        return

    changed_c_files = []
    for line in status.splitlines():
        fname = line[3:].strip()
        if fname.endswith(".c"):
            changed_c_files.append(Path(fname).name)

    pct = (completed / total * 100) if total > 0 else 0.0

    if custom_message:
        commit_msg = custom_message
    elif changed_c_files:
        if len(changed_c_files) == 1:
            clean_name = clean_problem_name(changed_c_files[0])
            commit_msg = f"feat(solution): solve {clean_name} [{completed}/{total} - {pct:.1f}%]"
        else:
            commit_msg = f"feat(solutions): solve {len(changed_c_files)} challenges [{completed}/{total} - {pct:.1f}%]"
    else:
        commit_msg = f"docs(progress): update progress & spaced repetition tracker [{completed}/{total} - {pct:.1f}%]"

    print(f"Staging changes with git add . ...")
    subprocess.run(["git", "add", "."], cwd=WORKSPACE, check=True)

    print(f"Committing: \"{commit_msg}\"")
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=WORKSPACE, check=True)

    if push:
        print("Pushing to remote origin (GitHub)...")
        push_res = subprocess.run(["git", "push", "origin", "main"], cwd=WORKSPACE, capture_output=True, text=True)
        if push_res.returncode == 0:
            print("✅ Successfully pushed to GitHub!")
        else:
            print(f"⚠️ Git push output: {push_res.stderr or push_res.stdout}")
    else:
        print("💡 Tip: Use `python sync_progress.py --push` to automatically push to GitHub.")

def main():
    parser = argparse.ArgumentParser(description="Sync C challenge tracking and Git repository.")
    parser.add_argument("-p", "--push", action="store_true", help="Push commit to remote GitHub repository.")
    parser.add_argument("--no-commit", action="store_true", help="Skip Git staging and committing.")
    parser.add_argument("-m", "--message", type=str, default=None, help="Custom Git commit message.")
    args = parser.parse_args()

    print("Scanning workspace for C challenge solutions...")
    c_files = find_c_files()
    print(f"Found {len(c_files)} verified .c solution(s).")

    # Step 1: Sync 250_C_QUESTIONS.md
    completed, total, stats = sync_250_questions(c_files)
    pct = (completed / total * 100) if total > 0 else 0.0
    print(f"Progress: {completed}/{total} ({pct:.2f}%)")

    # Step 2: Sync README.md
    sync_readme(completed, total, stats)

    # Step 3: Sync Spaced_Repetition_Tracker.md
    sync_spaced_tracker(c_files, stats)

    print("README.md, 250_C_QUESTIONS.md, & Spaced_Repetition_Tracker.md synchronized!")

    # Step 4: Git commit & push workflow
    if not args.no_commit:
        git_commit_and_push(custom_message=args.message, push=args.push, completed=completed, total=total)

if __name__ == "__main__":
    main()
