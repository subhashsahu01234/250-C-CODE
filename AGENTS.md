# 🤖 AGENTS.md — Coding Assistant Guidelines & Automation Rules

This document outlines the operational rules and automated maintenance procedures for any AI Coding Assistant (Antigravity, Gemini, etc.) working in this repository.

---

## 🎯 Primary Directives

Whenever you assist the user with solving, creating, reviewing, or debugging C challenge solutions in this repository, you must **automatically keep all tracking documentation in sync without requiring separate user prompts**.

---

## 🔄 Automatic Synchronization Checklist

When a challenge code file (e.g., `05_Array_Questions/Insert_an_element_in_an_array.c`) is written or completed:

### 1. Update `250_C_QUESTIONS.md`
- Locate the matching entry in [`250_C_QUESTIONS.md`](./250_C_QUESTIONS.md).
- Change `- [ ] filename.c` to `- [X] filename.c`.

### 2. Update `Spaced_Repetition_Tracker.md`
- Open [`Spaced_Repetition_Tracker.md`](./Spaced_Repetition_Tracker.md).
- If the problem is in `## ⏳ Pending — Not Yet Solved`, remove it from the pending list and insert a new row into the corresponding topic table.
- Populate the row:
  - **Problem Name**: Clean, human-readable name of the problem.
  - **Last Reviewed**: Current date (`YYYY-MM-DD`).
  - **Next Review**: Current date + 1 day (e.g., next day's date or `ASAP`).
  - **Interval**: `1 Day` (initial).
  - **Status / Notes**: Short summary of key algorithmic logic or edge cases.
- **When reviewing an existing problem:**
  - If solved successfully without hints: advance interval (`1 Day` → `3 Days` → `7 Days` → `14 Days` → `30 Days` → `🎓 Mastered`).
  - If struggled or made errors: reset interval to `1 Day`.

### 3. Update `README.md`
- Recalculate metrics in [`README.md`](./README.md):
  - Increment **Completed** count.
  - Decrement **Pending** count.
  - Update **Completion Percentage** (`(Completed / Total) * 100%`).
  - Update the visual text progress bar `[████...░░░░]`.
  - Update the specific topic row in the **Topic Breakdown Table** with the new `Solved / Total` count and status icon (`✅ Completed`, `⏳ In Progress`, `⭕ Not Started`).

### 4. Dynamic Auto-Sync & Git Commit
- Alternatively, run `python sync_progress.py` (or with `--push`) to automatically perform all markdown updates, recalculate progress, and commit changes with a descriptive message.


---

## 💻 C Code Quality Guidelines

When writing C solutions for this repository:
1. **Standard**: Adhere to modern standard C (C99 / C11).
2. **Signature**: Use `int main(void)` or `int main(int argc, char *argv[])` and explicitly `return 0;`.
3. **Safety & Robustness**:
   - Check return values of `scanf`, `malloc`, `fopen`, etc.
   - Prevent buffer overflows (e.g., use `fgets` instead of `gets` or unsafe `scanf("%s")`).
   - Free dynamically allocated memory.
4. **Documentation**:
   - Include a header comment at the top of each file stating the problem statement, expected input/output, and time/space complexity.
   - Keep comments concise and informative.

---

## 📂 Category Directory Map

All challenge files must be saved within their designated topic directory:

- `01_Simple_C_Questions/`
- `02_If_Else_Statement/`
- `03_Loops/While_Loop/`
- `03_Loops/Do_While_Loop/`
- `03_Loops/For_Loop/`
- `04_Switch_Case/`
- `05_Array_Questions/`
- `06_Matrix_Questions/`
- `07_String_Questions/`
- `08_String_Questions_Level_Up/`
- `09_Function_Questions/`
- `10_Pointer_Questions/`
- `11_File_Handling/`
- `12_Sorting/`
- `13_Searching/`
- `14_Tricky_Questions/`
- `15_Puzzles_Questions/`
