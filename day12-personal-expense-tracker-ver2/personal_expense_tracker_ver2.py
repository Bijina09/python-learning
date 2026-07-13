import sys
import os
from datetime import datetime, date

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

expenses = []

# Helper for checking empty input
def check_if_empty_input(prompt):
    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print(f"Input cannot be empty.\n")
        else:
            return entered_value

# Helper for displaying the question details
def display_expense_details(current_expense,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"Date : {current_expense['date']}\n"
    f"Category : {current_expense['category']}\n"
    f"Description : {current_expense['description']}\n"
    f"Amount : {current_expense['amount']}\n"
    )

def input_valid_date():

    while True: 
        entered_date = check_if_empty_input("Date (YY-MM-DD)")

        try:
            parsed_date = datetime.strptime(entered_date,"%Y-%m-%d").date()
            if parsed_date <= date.today():
                return parsed_date.strftime("%Y-%m-%d")
            else:
                raise ValueError("Date must not be in future")
        except ValueError as error:
            print(f"Invalid input: {error}. Please try again.")


def validate_integer(prompt):
    while True:
        try:
            entered_value = int(check_if_empty_input(prompt))
            return entered_value
        except ValueError:
            print("Input must be an integer.")

# Add Expense Function
def add_expense():
    
    clear_screen()

    expense_details = {}

    entered_date = input_valid_date()
    entered_category = check_if_empty_input("Category")
    entered_description = check_if_empty_input("Description")
    
    entered_amount = validate_integer("Amount")
    
    expense_details = {
        'date' : entered_date,
        'category' : entered_category,
        'description' : entered_description,
        'amount' : entered_amount
    }

    expenses.append(expense_details)

# View all Expenses function
def view_all_expenses():

    clear_screen()

    if not expenses:
        print("No Expenses Available.\n")
        return
    
    print("Expenses Details")
    for i, current_expense in enumerate(expenses, start=1):
        display_expense_details(current_expense,i=i)

# Search by Category function
def search_by_category():

    clear_screen()

    if not expenses:
        print("No Expenses Available.\n")
        return

    expense_to_search = check_if_empty_input("Category")

    i = 0
    for current_expense in expenses:
        if current_expense['category'].lower() == expense_to_search.lower():
            i += 1
            display_expense_details(current_expense,i)

    if i == 0:
        print("Expenses Not Found.\n")

# Deleting expense function
def delete_expense():

    clear_screen()

    if not expenses:
        print("No Expenses Available.\n")
        return

    while True:
        expense_to_delete = validate_integer("Expense Number")

        if 0 < expense_to_delete <= len(expenses):
            break
        else:
            print("Invalid expense number.")

    for i, current_expense in enumerate(expenses, start=1):
        if i == expense_to_delete:
            expenses.remove(current_expense)
            print("Expense deleted successfully.")
            return
    
    print("Expense Not Found.\n")

# Function for calculating total spending
def total_spending():

    clear_screen()

    if not expenses:
        print("No Expenses Available.\n")
        return

    total_amount = 0

    for current_expense in expenses:
        total_amount += current_expense['amount']
    
    print(f"Total Spending : Rs. {total_amount}\n")

# Function for calculating daily expense
def daily_expense_report():

    clear_screen()

    if not expenses:
        print("No Expenses Available.\n")
        return

    entered_date = input_valid_date()

    i = 0
    for current_expense in expenses:
        if current_expense['date'] == entered_date:
            i += 1
            display_expense_details(current_expense,i)
    
    if i == 0:
        print("Expenses Not Found.\n")

# Function for highest expense
def highest_expense():

    clear_screen()

    if not expenses:
        print("No Expenses Available.\n")
        return

    highest_amount = expenses[0]['amount']

    for current_expense in expenses:
        if current_expense['amount'] > highest_amount:
            highest_amount = current_expense['amount']
    
    print(f"Highest Expense : Rs. {highest_amount}\n")

    for current_expense in expenses:
        if current_expense['amount'] == highest_amount:
            display_expense_details(current_expense)
    
    

# Menu
def show_menu():
    print("===================Personal Expense Tracker Ver 2================\n")
    print("1. Add Expense\n" \
        "2. View All Expenses\n" \
        "3. Search By Category\n" \
        "4. Delete Expense\n" \
        "5. Total Spending\n" \
        "6. Daily Expense Report\n" \
        "7. Highest Expense\n" \
        "8. Exit\n\n" \
        "Enter your choice: ")
    
# Main function
def main():

    while True:

        clear_screen()

        show_menu()

        try:
            choice = int(input())
        except ValueError:
            print("\nError: Please enter a valid integer\n")
            input("\nPress enter to continue")
        else:
            match choice:
                case 1:
                    add_expense()
                case 2:
                    view_all_expenses()
                case 3:
                    search_by_category()
                case 4:
                    delete_expense()
                case 5:
                    total_spending()
                case 6:
                    daily_expense_report()
                case 7:
                    highest_expense()
                case 8:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()