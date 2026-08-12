from collections import defaultdict
from datetime import datetime

# function to add an expense
def add_expense():
    while True:
        category = input("Enter category of expense: ").lower()
        if category:     # validating empty input
            break
        print("Please enter strings/words.")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            
            # validating negative input
            if amount > 0:
                break
            print("Amount cannot be negative!")
        except ValueError:
            print("Enter an integer value.")


    present = datetime.now()

    # return the data to store
    new_expense = {"category": category,
                   "amount": amount,
                   "date": f"{present.strftime("%d-%m-%Y")}"}
    
    return new_expense

# Function to View All expenses
def view_expenses(expense_list):
    for expense in expense_list:
        print(f"----{expense["category"]}----")
        print(f"₹{expense["amount"]}")
        print(f"{expense["date"]}")

# function to calculate total and maximum spent category
def total_and_highest(expense_list):

    # groupping by category through collections
    my_dict = defaultdict(list)
    for item in expense_list:
        my_dict[item['category']].append(item)

    # track maximum amount and category
    max_total = -1
    max_category = None

    for key, value in my_dict.items():
        print(f"\nCategory: {key}")
        for expense in value:
                print(f" ₹{expense['amount']}")

        # compute total for each category
        total = sum(item["amount"] for item in value)
        print(f"Total = ₹{float(total)}")

        # check if this category is maximum overall
        if total > max_total:
            max_total = total
            max_category = key     # key is category

    print(f"Highest Spending: ₹{max_total} on {max_category}")

# Print the monthlt summary
def monthly_summary(expense_list):
    # Dictionary to store month_year -> total_amount
    monthly_totals = defaultdict(float)

    for expense in expense_list:

        # split the date parts
        date_parts = expense["date"].split("-")
        
        # Extract month and year (parts at index 1 and 2)
        month = date_parts[1]
        year = date_parts[2]
        
        # Create a clean key
        month_key = f"{month}-{year}"
        
        # Add to total
        monthly_totals[month_key] += expense["amount"]

    # Display results
    print("\n----- MONTHLY SUMMARY -----")
    for month_year, total in monthly_totals.items():
        print(f"Month ({month_year}): ₹{total:.2f}")

    return monthly_totals

def delete_expense(expense_list):
    if not expense_list:
        print("\nNo expenses found to delete!")
        return expense_list

    # 1. Display expenses with index numbers
    print("\n----- DELETE EXPENSE -----")
    for index, expense in enumerate(expense_list, start=1):
        print(f"{index}. Category: {expense['category']} | Amount: ₹{expense['amount']} | Date: {expense['date']}")

    # 2. Get user choice with error handling
    try:
        choice = int(input("\nEnter the number of the expense to delete: "))
        
        if 1 <= choice <= len(expense_list):
            # Convert 1-based index to 0-based index
            deleted = expense_list.pop(choice - 1)
            print(f" Successfully deleted: {deleted['category']} (₹{deleted['amount']})")
        else:
            print("❌ Invalid expense number.")
            
    except ValueError:
        print("❌ Please enter a valid number.")

    return expense_list

def edit_expense(expense_list):
    if not expense_list:
        print("\nNo expenses found to edit!")
        return expense_list

    # 1. Display expenses with index numbers
    print("\n----- EDIT EXPENSE -----")
    for index, expense in enumerate(expense_list, start=1):
        print(f"{index}. Category: {expense['category']} | Amount: ₹{expense['amount']} | Date: {expense['date']}")

    # 2. Get user choice
    try:
        choice = int(input("\nEnter the number of the expense to edit: "))
        
        if 1 <= choice <= len(expense_list):
            target = expense_list[choice - 1]
            print("\n(Press Enter to keep the current value)")

            # Edit Category
            new_cat = input(f"New category [{target['category']}]: ").strip()
            if new_cat:
                target['category'] = new_cat

            # Edit Amount
            new_amt = input(f"New amount [{target['amount']}]: ").strip()
            if new_amt:
                try:
                    target['amount'] = float(new_amt)
                except ValueError:
                    print("⚠️ Invalid amount entered. Keeping old amount.")

            # Edit Date
            new_date = input(f"New date [{target['date']}]: ").strip()
            if new_date:
                target['date'] = new_date

            print("\n Expense updated successfully!")
        else:
            print("❌ Invalid expense number.")

    except ValueError:
        print("❌ Please enter a valid number.")

    return expense_list

