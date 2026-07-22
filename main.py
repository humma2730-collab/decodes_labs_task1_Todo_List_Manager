"""
--------------------------------------------
File:         main.py
Project:      To-Do List Manager
Description:  Main program entry point.
Developed by: Huma Fatima
--------------------------------------------
"""1

from task_manager import (
    add_task,
    view_tasks,
    update_task,
    delete_task,
    mark_task_completed,
    search_task,
    task_statistics,
)

# Display Menu

def display_menu():
    print("\n" + "*" * 40)
    print("        TO-DO LIST MANAGER")
    print("*" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Search Task")
    print("7. Task Statistics")
    print("8. Exit")
    print("*" * 40)

# Main Function

def main():

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            mark_task_completed()

        elif choice == "6":
            search_task()

        elif choice == "7":
            task_statistics()

        elif choice == "8":
            print("\nThank you for using To-Do List Manager.")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()