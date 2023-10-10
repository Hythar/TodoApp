# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to view the to-do list
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to remove a task from the to-do list
def remove_task(task_index):
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(todo_list):
            removed_task = todo_list.pop(task_index - 1)
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid task index.")

# Main program loop
while True:
    print("\nOptions:")
    print("Enter 'add' to add a task")
    print("Enter 'view' to view tasks")
    print("Enter 'remove' to remove a task")
    print("Enter 'quit' to exit")
    
    user_input = input("Your choice: ").lower()
    
    if user_input == "add":
        task = input("Enter the task: ")
        add_task(task)
    elif user_input == "view":
        view_tasks()
    elif user_input == "remove":
        task_index = input("Enter the index of the task to remove: ")
        remove_task(task_index)
    elif user_input == "quit":
        break
    else:
        print("Invalid input. Please try again.")
