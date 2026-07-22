"""
------------------------------------------
File:         task_manager.py
Project:      To-Do List Manager
Description:  Task management functions.
Developed by: Huma Fatima
------------------------------------------
"""

from datetime import datetime
from file_handler import load_tasks, save_tasks

# Generate Next Task ID
def generate_task_id(tasks):

    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

# Add Task
def add_task():

    tasks = load_tasks()
    print("\n******** ADD NEW TASK *********")
    title = input("Enter Task Title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    task = {
        "id": generate_task_id(tasks),
        "title": title,
        "status": "Pending",
        "created_at": current_time,
        "updated_at": current_time
    }
    tasks.append(task)
    save_tasks(tasks)
    print("\nTask added successfully!")

# View Tasks
def view_tasks():
    
    tasks = load_tasks()
    print("\n********* ALL TASKS **********")
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print("-" * 50)
        print(f"Task ID      : {task['id']}")
        print(f"Title        : {task['title']}")
        print(f"Status       : {task['status']}")
        print(f"Created At   : {task['created_at']}")
        print(f"Updated At   : {task['updated_at']}")
    print("-" * 50)

# Update Task
def update_task():
    
    tasks = load_tasks()

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("\nEnter Task ID to Update: "))
    except ValueError:
        print("Invalid Task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:

            new_title = input("Enter New Task Title: ").strip()

            if not new_title:
                print("Task title cannot be empty.")
                return

            current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            task["title"] = new_title
            task["updated_at"] = current_time
            save_tasks(tasks)
            print("\nTask updated successfully!")
            return

    print("Task ID not found.")

# Delete Task
def delete_task():

    tasks = load_tasks()

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("\nEnter Task ID to Delete: "))
    except ValueError:
        print("Invalid Task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:

            confirm = input(
                f"Are you sure you want to delete '{task['title']}'? (y/n): "
            ).strip().lower()

            if confirm == "y":
                tasks.remove(task)
                save_tasks(tasks)
                print("\nTask deleted successfully!")
            else:
                print("\nDelete cancelled.")
            return
    print("Task ID not found.")
    
# Mark Task as Completed

def mark_task_completed():
    """
    Mark a task as completed.
    """
    tasks = load_tasks()

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("\nEnter Task ID to Mark Complete: "))
    except ValueError:
        print("Invalid Task ID.")
        return

    for task in tasks:

        if task["id"] == task_id:

            if task["status"] == "Completed":
                print("\nTask is already completed.")
                return

            task["status"] = "Completed"
            task["updated_at"] = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

            save_tasks(tasks)

            print("\nTask marked as completed successfully!")
            return

    print("Task ID not found.")
# Search Task

def search_task():

    tasks = load_tasks()

    if not tasks:
        print("\nNo tasks available.")
        return

    keyword = input("\nEnter task title to search: ").strip().lower()

    if not keyword:
        print("Search text cannot be empty.")
        return

    found = False

    print("\n******** SEARCH RESULTS ********")

    for task in tasks:

        if keyword in task["title"].lower():

            found = True

            print("-" * 50)
            print(f"Task ID    : {task['id']}")
            print(f"Title      : {task['title']}")
            print(f"Status     : {task['status']}")
            print(f"Created At : {task['created_at']}")
            print(f"Updated At : {task['updated_at']}")

    if not found:
        print("No matching task found.")

    print("-" * 50)

# Task Statistics
def task_statistics():
    
    tasks = load_tasks()

    total = len(tasks)

    completed = sum(
        1 for task in tasks
        if task["status"] == "Completed"
    )
    pending = total - completed
    print("\n*********  TASK STATISTICS   **********")
    print(f"Total Tasks      : {total}")
    print(f"Completed Tasks  : {completed}")
    print(f"Pending Tasks    : {pending}")