# 🚀 250+ C Programming Mastery Challenges

A curated, comprehensive roadmap of 250+ fundamental and advanced C programming problems designed to build deep algorithmic intuition, memory mastery, and mastery of low-level C concepts.

---

## 📊 Progress Dashboard

| Metric | Status |
| :--- | :--- |
| **Total Challenges** | `234` |
| **Completed** | `21` |
| **Pending** | `213` |
| **Current Completion Rate** | `8.97%` |

```text
Progress: [████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 8.97% (21 / 234)
```

---

## 🗂️ Core Tracking Documents

- 📋 **[250_C_QUESTIONS.md](./250_C_QUESTIONS.md)** — Complete checklist of all 250+ problems categorized by topic.
- 🧠 **[Spaced_Repetition_Tracker.md](./Spaced_Repetition_Tracker.md)** — Ebbinghaus forgetting curve schedule (1d → 3d → 7d → 14d → 30d → Mastered).
- 🤖 **[AGENTS.md](./AGENTS.md)** — Automation rules for AI coding assistants to keep checklists, stats, and spaced reviews automatically synchronized.

---

## 📁 Repository Structure & Topic Breakdown

| # | Topic / Folder | Status | Solved / Total |
| :-: | :--- | :-: | :-: |
| 01 | [`01_Simple_C_Questions`](./01_Simple_C_Questions/) | ⏳ In Progress | 6 / 12 |
| 02 | [`02_If_Else_Statement`](./02_If_Else_Statement/) | ⏳ In Progress | 12 / 28 |
| 03 | [`03_Loops`](./03_Loops/) (`While_Loop`, `Do_While_Loop`, `For_Loop`) | ⏳ In Progress | 1 / 17 |
| 04 | [`04_Switch_Case`](./04_Switch_Case/) | ⏳ In Progress | 1 / 12 |
| 05 | [`05_Array_Questions`](./05_Array_Questions/) | ⭕ Not Started | 0 / 24 |
| 06 | [`06_Matrix_Questions`](./06_Matrix_Questions/) | ⏳ In Progress | 1 / 18 |
| 07 | [`07_String_Questions`](./07_String_Questions/) | ⭕ Not Started | 0 / 16 |
| 08 | [`08_String_Questions_Level_Up`](./08_String_Questions_Level_Up/) | ⭕ Not Started | 0 / 25 |
| 09 | [`09_Function_Questions`](./09_Function_Questions/) | ⭕ Not Started | 0 / 32 |
| 10 | [`10_Pointer_Questions`](./10_Pointer_Questions/) | ⭕ Not Started | 0 / 16 |
| 11 | [`11_File_Handling`](./11_File_Handling/) | ⭕ Not Started | 0 / 21 |
| 12 | [`12_Sorting`](./12_Sorting/) | ⭕ Not Started | 0 / 7 |
| 13 | [`13_Searching`](./13_Searching/) | ⭕ Not Started | 0 / 3 |
| 14 | [`14_Tricky_Questions`](./14_Tricky_Questions/) | ⭕ Not Started | 0 / 2 |
| 15 | [`15_Puzzles_Questions`](./15_Puzzles_Questions/) | ⭕ Not Started | 0 / 1 |

---

## 🛠️ How to Compile and Run

To compile and run any C challenge file:

```bash
# Using GCC:
gcc -Wall -Wextra -std=c11 <filename>.c -o output.exe
./output.exe

# Using Clang:
clang -Wall -Wextra -std=c11 <filename>.c -o output.exe
./output.exe
```

---

## 💻 C Code Quality Standards

All solutions in this repository follow these guidelines (see [AGENTS.md](./AGENTS.md) for full details):

| Guideline | Detail |
| :--- | :--- |
| **Standard** | Modern C (C99 / C11) |
| **Main signature** | `int main(void)` or `int main(int argc, char *argv[])` with explicit `return 0;` |
| **Input safety** | Check return values of `scanf`, `malloc`, `fopen`, etc. |
| **Buffer safety** | Use `fgets` instead of unsafe `gets`; bounds-check arrays |
| **Memory management** | Free all dynamically allocated memory (`free(ptr)`) |

---

## 🧠 Spaced Repetition Workflow

This project uses a **spaced repetition** system based on the Ebbinghaus forgetting curve to move solutions from short-term recall into long-term mastery.

**Interval progression:** `1 Day` → `3 Days` → `7 Days` → `14 Days` → `30 Days` → `🎓 Mastered`

1. **Solve** a problem in its topic directory.
2. **Mark as done** `- [X]` in [`250_C_QUESTIONS.md`](./250_C_QUESTIONS.md).
3. **Register** the review date in [`Spaced_Repetition_Tracker.md`](./Spaced_Repetition_Tracker.md).
4. **Review** on scheduled days — if solved cleanly, advance the interval; if you struggle, reset to `1 Day`.

---

## ⚡ Automated Sync Script

Run the sync script to keep all tracking documents in sync automatically:

```bash
# Sync progress locally (marks completed, updates stats)
python sync_progress.py

# Sync and push to GitHub
python sync_progress.py --push
```

**What it does:**
- Verifies `.c` files contain valid solution code
- Marks completed problems `- [X]` in `250_C_QUESTIONS.md`
- Registers new problems in `Spaced_Repetition_Tracker.md` (initial 1-day interval)
- Updates the progress bar and topic breakdown in this README
- Stages and commits with semantic messages (e.g., `feat(solution): solve <Problem> [21/234 - 8.97%]`)

---

## 🤖 AI Assistant Mode

This repository is configured for **mentor-only** AI assistance (see [AGENTS.md](./AGENTS.md)):

- ❌ The AI will **not** generate or solve challenge code autonomously
- ✅ The AI **will** provide hints, pseudocode outlines, and edge-case guidance
- ✅ The AI **will** review your code for bugs, logic errors, and memory leaks
- ✅ The AI **will** update spaced repetition schedules after review sessions
