import sys

expenses = []

def clear_screen():
    print("\033[H\033[J", end="")

def add_expense():
    
    clear_screen()

    expense_details = {}

    expense_details['category'] = input("Category: ")
    expense_details['amount'] = int(input("\nAmount: "))
    expense_details['description'] = input("\nDescription: ")

    expenses.append(expense_details)

def view_expenses():

    clear_screen()

    if not expenses:
        print("\nNo expenses Found.")
        return

    for i, current_expense in enumerate(expenses):

        print(f"{i+1}.\n\n"
            f"Category : {current_expense['category']}\n"
            f"Amount : {current_expense['amount']}\n"
            f"Description : {current_expense['description']}\n\n\n")

    

def search_by_category():
    
    clear_screen()

    to_search = input("Enter the category: ")

    expense_found = False 

    for current_expense in expenses:
        if current_expense['category'].lower() == to_search.lower():
            expense_found = True
            print(f"\nCategory : {current_expense['category']}\n"
                  f"Amount : {current_expense['amount']}\n"
                  f"Description : {current_expense['description']}\n\n"
                )

    if not expense_found:
        print("\nNo expenses Found.")

def show_total_spending():

    clear_screen()

    total_spending = 0

    for current_expense in expenses:
        total_spending += current_expense['amount']
    
    print(f"Total Spending\n Rs. {total_spending}")


def show_highest_expense():

    clear_screen()

    if not expenses:
        print("\nNo expenses currently listed.")
        return
    else:
        highest_expense = expenses[0]['amount']

    for current_expense in expenses:
        if current_expense['amount'] > highest_expense:
            highest_expense = current_expense['amount']

    print("Highest Expense\n\n")
    for current_expense in expenses:
        if current_expense['amount'] == highest_expense:

            print(f"Category: {current_expense['category']}\n"
                    f"Amount : {current_expense['amount']}\n"
                    f"Description : {current_expense['description']}\n\n"
                )


def show_menu():
    print("==================Expense Tracker===============\n\n" \
    "1. Add Expense\n" \
    "2. View Expenses\n" \
    "3. Search by Category\n" \
    "4. Show Total Spending\n" \
    "5. Show Highest Expense\n" \
    "6. Exit\n\n" \
    "Enter your choice: ")

def main():
 
    while True: 

        clear_screen()

        show_menu()

        choice = int(input())

        match choice:
            case 1:
                add_expense()
            case 2:
                view_expenses()
            case 3:
                search_by_category()
            case 4:
                show_total_spending()
            case 5:
                show_highest_expense()
            case 6:
                sys.exit(0)
            case _:
                print("Invalid Choice")

        input("\n\nPlease press enter to go back to the menu.")

main()