#lets create a to-do list 
print("Welcome to our to-do list.")


def display_todo():
    #displaying menu to the user
    print("\n [1] Add Task.")
    print("[2] View Task.")
    print("[3] Delete Task.")
    print("[4] Exit")


def add():
    
    task = input("Enter your new task: ")

    deadline_choice = input("Do you want to add a deadline? (1 for yes, 0 for no): ")

    if deadline_choice == "1":
        deadline = input("Enter your deadline: ")
        full_task = f"{task} | Deadline: {deadline}\n"
    else:
        full_task = f"{task} | No deadline\n"

    with open("TODO.txt", "a") as file:
        file.write(full_task)

    print("Your task has been added.")


def view():
    
    try:
        with open("TODO.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")
    except FileNotFoundError:
        print("No to-do list file found yet.")

def delete ():
    with open("TODO.txt", "r") as file:
        tasks = file.readlines()

    if not tasks: 
        print("Your list is empty.")
    else: 
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.strip()}")
    task_num = int(input("Enter the task number to delete: "))
    deleted_task = tasks.pop(task_num - 1)
    with open("TODO.txt", "w") as file:
        file.writelines(tasks)
    print(f"Deleted task: {deleted_task.strip()}")



while True: 
       display_todo()  # show menu

       choice = input("Enter your choice: ")

       if choice == "1":
           add()  # (you'll define this)
       elif choice == "2":
            view()
       elif choice == "3":
            delete()
       elif choice == "4":
            print("Exiting... Goodbye!")
            break
       else:
            print("Invalid choice. Please select from 1 to 4.")










        







