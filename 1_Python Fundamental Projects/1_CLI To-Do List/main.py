from storage import load_data, save_data
from utils import add_task, view_task, mark_completed, edit_task, delete_task

task_list = load_data()    # Creates json file if run for first time

while True:
    print("-----------MENU-----------")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Completed")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Save and Exit")

    try:
        choice = int(input("Enter your Choice: "))
    except ValueError:                # handles invalid input
        print("Please Enter Valid option.")
        continue

    # Add task
    if choice == 1:
        new_task = add_task()
        task_list.append(new_task)
        print("New Task Added Successfully!")

    # View All Task
    elif choice == 2:
        if not task_list:
            print("No Task Records!")
            continue
        view_task(task_list)

    # Mark task as completed
    elif choice == 3:
        if not task_list:
            print("No Records Found!")
            continue
        else:
            mark_completed(task_list)

    # Edit Task
    elif choice == 4:
        if not task_list:
            print("No Records Found!")
            continue
        else:
            edit_task(task_list)

    elif choice == 5:
        if not task_list:
            print("No Records Found!")
            continue
        else:
            delete_task(task_list)

    elif choice == 6:
        save_data(task_list)     # Saves to json as Exit
        break


