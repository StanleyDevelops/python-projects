from datetime import datetime    # to store dates

def add_task():
    while True:
        title = input("Enter Title: ")
        if title:
            break
        print("Title cannot be empty")
  
    description = input("Enter Description: ")  

    present = datetime.now()
    date  = present.strftime("%d-%m-%Y")       # storing date of adding task

    return {"title": title,
            "description": description,
            "status": "🟡pending",
            "date": date}
        
def view_task(data):
    for i, task in enumerate(data):
        print(f"{i+1}. {task['title']}")
        print(f"***{task["description"]}***")
        print(f"Status: {task["status"]}")
        print(f"Due Date: {task["date"]}")

def mark_completed(task_list):
    search_task = input("Enter Task to mark Completed: ").lower()  
    for task in task:
        if task["title"].lower() == search_task:
            task["status"] = "✓Completed"
            print("Marked Completed Successfully")
            break
    else:
        print("Task Not Found!")

def edit_task(task_list):
    search_title = input("Enter title to edit: ")    # Better version to choose by index
    for task in task_list:
        if task["title"].lower() == search_title.lower():
            new_description = input("Enter new Description: ")
            task["description"] = new_description
            print("Task Edited Successfully!")
            break
    else:
        print("Searched Task Not Found!")

def delete_task(task_list):
    search_to_delete = input("Enter Task Title to delete: ").lower()
    for task in task_list:
        if task["title"].lower() == search_to_delete:
            task_list.remove(task)
            print("Task Deleted Successfully!")
            break
    else:
        print("Title not Found in Records!")
