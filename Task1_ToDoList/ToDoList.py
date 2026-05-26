# ============================================================
#  CodSoft Internship - Task 1: TO-DO LIST
#  Author  : Srushti patil
#  Language: Python 3
#  Run     : python todo_list.py
# ============================================================

import os
import json
from datetime import datetime

# ---------- File to save tasks (persistent storage) ----------
DATA_FILE = "tasks.json"

# ---------- Load tasks from file ----------
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# ---------- Save tasks to file ----------
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# ---------- Display all tasks ----------
def show_tasks(tasks, filter_by="all"):
    print("\n" + "=" * 55)
    print(f"{'📋  YOUR TO-DO LIST':^55}")
    print("=" * 55)

    filtered = []
    for t in tasks:
        if filter_by == "all":
            filtered.append(t)
        elif filter_by == "active" and not t["done"]:
            filtered.append(t)
        elif filter_by == "completed" and t["done"]:
            filtered.append(t)

    if not filtered:
        print("  No tasks found.")
    else:
        for i, task in enumerate(filtered, 1):
            status  = "✅" if task["done"] else "⬜"
            priority = task.get("priority", "Medium")
            category = task.get("category", "General")
            date     = task.get("date", "")
            print(f"  {i}. {status} [{priority:6}] [{category:10}] {task['text']}")
            if date:
                print(f"       📅 Added: {date}")

    done_count  = sum(1 for t in tasks if t["done"])
    total_count = len(tasks)
    print("-" * 55)
    print(f"  Total: {total_count}  |  Done: {done_count}  |  Remaining: {total_count - done_count}")
    print("=" * 55)

# ---------- Add a new task ----------
def add_task(tasks):
    print("\n--- ADD TASK ---")
    text = input("  Enter task description: ").strip()
    if not text:
        print("  ⚠️  Task cannot be empty.")
        return

    print("  Categories: Personal | Work | Study | Other")
    category = input("  Enter category (default=General): ").strip() or "General"

    print("  Priorities: High | Medium | Low")
    priority = input("  Enter priority (default=Medium): ").strip() or "Medium"
    if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"

    task = {
        "id"      : len(tasks) + 1,
        "text"    : text,
        "category": category,
        "priority": priority,
        "done"    : False,
        "date"    : datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"  ✅ Task added: '{text}'")

# ---------- Mark task as complete ----------
def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\n  Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"  ✅ Task {num} marked as completed!")
        else:
            print("  ⚠️  Invalid number.")
    except ValueError:
        print("  ⚠️  Please enter a valid number.")

# ---------- Edit a task ----------
def edit_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\n  Enter task number to edit: "))
        if 1 <= num <= len(tasks):
            new_text = input(f"  New description (current: '{tasks[num-1]['text']}'): ").strip()
            if new_text:
                tasks[num - 1]["text"] = new_text
                save_tasks(tasks)
                print("  ✅ Task updated!")
            else:
                print("  ⚠️  No changes made.")
        else:
            print("  ⚠️  Invalid number.")
    except ValueError:
        print("  ⚠️  Please enter a valid number.")

# ---------- Delete a task ----------
def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\n  Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"  🗑️  Deleted: '{removed['text']}'")
        else:
            print("  ⚠️  Invalid number.")
    except ValueError:
        print("  ⚠️  Please enter a valid number.")

# ---------- Clear completed tasks ----------
def clear_completed(tasks):
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t["done"]]
    save_tasks(tasks)
    print(f"  🧹 Cleared {before - len(tasks)} completed task(s).")

# ---------- Main Menu ----------
def main():
    tasks = load_tasks()
    print("\n  Welcome to TaskFlow - To-Do List App")
    print("  CodSoft Python Internship - Task 1")

    while True:
        print("\n" + "-" * 40)
        print("  MENU")
        print("  1. View All Tasks")
        print("  2. View Active Tasks")
        print("  3. View Completed Tasks")
        print("  4. Add Task")
        print("  5. Complete a Task")
        print("  6. Edit a Task")
        print("  7. Delete a Task")
        print("  8. Clear Completed Tasks")
        print("  9. Exit")
        print("-" * 40)

        choice = input("  Choose an option (1-9): ").strip()

        if choice == "1":
            show_tasks(tasks, "all")
        elif choice == "2":
            show_tasks(tasks, "active")
        elif choice == "3":
            show_tasks(tasks, "completed")
        elif choice == "4":
            add_task(tasks)
        elif choice == "5":
            complete_task(tasks)
        elif choice == "6":
            edit_task(tasks)
        elif choice == "7":
            delete_task(tasks)
        elif choice == "8":
            clear_completed(tasks)
        elif choice == "9":
            print("\n  👋 Goodbye! Stay productive!\n")
            break
        else:
            print("  ⚠️  Invalid choice. Please enter 1-9.")

# ---------- Entry Point ----------
if __name__ == "__main__":
    main()
