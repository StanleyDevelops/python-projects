# MINI EXPENSE TRACKER
from utils import add_expense, total_and_highest, delete_expense, edit_expense
from utils import view_expenses, monthly_summary
from json_storage import load_data, save_data

expenses = load_data()    # load the existing file or create a new one

while True:
    print("_-_-_-_-_-_-_-_- MENU -_-_-_-_-_-_-_-_")
    print("1. Add an expense")
    print("2. View All Expenses")
    print("3. Total and Highest Spending")
    print("4. Monthly Summary")
    print("5. Delete Expenses")
    print("6. Edit Expense")
    print("7. Save and Exit")

    try:
        option = int(input("Enter your choice here: "))
    except ValueError:
        print("Please enter valid option!")
        continue

    if option == 1:
        new_expense = add_expense()
        expenses.append(new_expense)
        print(f"{new_expense['category']} Added to the List.")

    elif option == 2:
        view_expenses(expenses)

    elif option == 3:
        if not expenses:
            print("There's no record of groceries!")
            continue
        else:
            total_and_highest(expenses)

    elif option == 4:
        if not expenses:
            print("There's no record of groceries!")
            continue
        else:
            monthly_summary = monthly_summary(expenses)

    elif option == 5:
        expenses = delete_expense(expenses)

    elif option == 6:
        expenses = edit_expense(expenses)

    elif option == 5:
        print("Expenses Saved.")
        print("Exiting...")
        save_data(expenses)
        break

    else:
        print("Invalid Input.")


        