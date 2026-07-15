import sys
import os

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

accounts = []

# Helper for checking empty input
def check_if_empty_input(prompt):
    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print(f"Input cannot be empty.\n")
        else:
            return entered_value
        
# Helper for displaying the account details
def display_account_details(current_account,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"\nAccount No : {current_account['account_no']}\n"
    f"Name : {current_account['name']}\n"
    f"Balance : Rs. {current_account['balance']}\n")

def validate_integer(prompt):
    while True:
        try:
            entered_value = int(check_if_empty_input(prompt))
            return entered_value
        except ValueError:
            print("Input must be an integer.\n")

def duplicate_account_check(prompt):

    while True:
        duplicate_exists = False

        entered_account_no = validate_integer(prompt)

        for current_account in accounts:
            if current_account['account_no'] == entered_account_no:
                print("Account already exists.\n")
                duplicate_exists = True
                break

        if not duplicate_exists:
            return entered_account_no

def find_account(account_no):

    for current_account in accounts:
        if current_account['account_no'] == account_no:
            return current_account

    return False     

def check_positive(prompt):

    while True:
        entered_amount = validate_integer(prompt)
        if entered_amount > 0:
            return entered_amount
        else:
            print("Amount must be positive.\n")

def create_account():

    clear_screen()

    entered_account_no = duplicate_account_check("Account No.")

    entered_name = check_if_empty_input("Name")
    entered_balance = check_positive("Balance")

    account_details = {
        'account_no' : entered_account_no,
        'name' : entered_name,
        'balance' : entered_balance
    }

    accounts.append(account_details)
    print("\nAccount created successfully.\n")

# View all Books function
def view_all_accounts():

    clear_screen()

    if not accounts:
        print("No Accounts Available.\n")
        return
    
    print("Account Details")
    for i, current_account in enumerate(accounts, start=1):
        display_account_details(current_account,i=i)

def search_account():

    clear_screen()

    if not accounts:
        print("Accounts Not Available.\n")
        return
    
    to_search = validate_integer("Account No.")

    for current_account in accounts:
        if current_account['account_no'] == to_search:
            display_account_details(current_account)
            return
    
    print("Account Not Found.")
    

def deposit_money():

    clear_screen()

    if not accounts:
        print("No Accounts Available.\n")
        return
    
    to_deposit_account = validate_integer("Account No.")

    account = find_account(to_deposit_account)

    if not account:
        print("Account Not Found.\n")
        return

    to_deposit_amount = check_positive("Deposit Amount")

    account['balance'] += to_deposit_amount
    print("Amount deposited successfully.\n")
    return
        
def withdraw_money():

    clear_screen()

    if not accounts:
        print("No Accounts Available.\n")
        return
    
    to_withdraw_account = validate_integer("Account No.")

    account = find_account(to_withdraw_account)
    if not account:
        print("Account Not Found.\n")
        return

    to_withdraw_amount = check_positive("Withdraw Amount")
    
    if account['balance'] >= to_withdraw_amount:
        account['balance'] -= to_withdraw_amount
        print("Amount withdrawn successfully.\n")
        return
    else:
        print("Insufficient balance.\n")
        return

def delete_account():

    clear_screen()

    if not accounts:
        print("Accounts Not Available.\n")
        return

    to_delete = validate_integer("Account No.")

    account = find_account(to_delete)
    if not account:
        print("Account Not Found.\n")
        return

    accounts.remove(account)
    print(f"\nAccount No. {to_delete} deleted successfully.")
    return

def view_total_balance():

    clear_screen()

    if not accounts:
        print("Accounts Not Available.\n")
        return

    total_balance = 0

    for current_account in accounts:
        total_balance += current_account['balance']

    print(f"Total Balance in the Bank : Rs. {total_balance}")
        

def show_menu():
    print("===================Bank Account Management System================\n\n")
    print("1. Create Account\n" \
        "2. View All Accounts\n" \
        "3. Search Account\n" \
        "4. Deposit Money\n" \
        "5. Withdraw Money\n"
        "6. Delete Account\n"
        "7. View Total Balance in Bank\n"
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
                    create_account()
                case 2:
                    view_all_accounts()
                case 3:
                    search_account()
                case 4:
                    deposit_money()
                case 5:
                    withdraw_money()
                case 6:
                    delete_account()
                case 7:
                    view_total_balance() 
                case 8:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()