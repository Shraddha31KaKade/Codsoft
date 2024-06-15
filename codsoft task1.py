import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i+1}. {task['task']} - {status}")

def update_task(tasks, index, new_task):
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def mark_task_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '3':
            view_tasks(tasks)
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            update_task(tasks, index, new_task)
        elif choice == '4':
            view_tasks(tasks)
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '5':
            view_tasks(tasks)
            index = int(input("Enter the task number to mark as completed: ")) - 1
            mark_task_completed(tasks, index)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()