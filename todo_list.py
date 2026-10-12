# To-Do List CLI App
# CodeOrbit Tech - Python Programming Internship

tasks = []


# Function to add a task
def add_task():
    task = input("Enter a task: ")

    if task.strip():
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


# Function to remove a task
def remove_task():
    view_tasks()

    if tasks:
        try:
            number = int(input("Enter the task number to remove: "))

            if 1 <= number <= len(tasks):
                removed_task = tasks.pop(number - 1)
                print(f"Removed: {removed_task}")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


# Main program
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")