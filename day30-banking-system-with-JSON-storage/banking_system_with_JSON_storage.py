import os
import sys
import json

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

# Helper for checking empty input
def check_if_empty_input(prompt):
    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print(f"Input cannot be empty.\n")
        else:
            return entered_value
        
def validate_integer(prompt):
    while True:
        try:
            entered_value = int(check_if_empty_input(prompt))
            return entered_value
        except ValueError:
            print("Input must be an integer.\n")

def validate_positive_balance(prompt):
  while True:
      entered_value = validate_integer(prompt)
      if entered_value > 0:
         return entered_value
      else:
          print("Amount must be greater than zero.\n")

# Helper for displaying the account details
def display_account_details(current_account,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    "---------------------------------------"
    f"\nAccount No : {current_account['account_no']}\n"
    f"Name : {current_account['name']}\n"
    f"Balance : {current_account['balance']}\n")

        
class BankSystem:   

    def __init__(self):
        self.accounts = []
        self.load_data()

    def duplicate_account_check(self, prompt, account=None):

        while True:
            duplicate_exists = False

            entered_account_no = validate_integer(prompt)

            for current_account in self.accounts:
                if current_account['account_no'] == entered_account_no:
                    if current_account is account:
                        continue
                    print("Account already exists.\n")
                    duplicate_exists = True
                    break

            if not duplicate_exists:
                return entered_account_no

    def find_account(self,account_no):

        for current_account in self.accounts:
            if current_account['account_no'] == account_no:
                return current_account

        return False

    def create_account(self):

        clear_screen()

        entered_account_no = self.duplicate_account_check("Account No")
        entered_name = check_if_empty_input("Name")
        entered_balance = validate_positive_balance("Initial Balance")
        
        account_details = {
            'account_no' : entered_account_no,
            'name' : entered_name,
            'balance' : entered_balance
        }

        self.accounts.append(account_details)

        print("\nAccount created successfully.\n")

        self.save_data()
        
    def view_accounts(self):

        clear_screen()
        
        if not self.accounts:
            print("No accounts available.\n")
            return
            
        print("Account Details")
        for i, current_account in enumerate(self.accounts, start=1):
            display_account_details(current_account,i=i)

    def search_account(self):

        clear_screen()
    
        if self.check_if_empty():
            return
        
        to_search = validate_integer("Account No")
    
        account = self.find_account(to_search)
    
        if not account:
            print("Account not found.")
            return
    
        display_account_details(account)

    def deposit_money(self):

        clear_screen()
    
        if self.check_if_empty():
            return
        
        to_deposit_account = validate_integer("Account No")
    
        account = self.find_account(to_deposit_account)
    
        if not account:
            print("Account not found.\n")
            return

        account['balance'] += validate_positive_balance("Amount")
    
        print("\nAmount deposited successfully.")

        self.save_data()

    def withdraw_money(self):

        clear_screen()
    
        if self.check_if_empty():
            return
        
        to_withdraw_account = validate_integer("Account No")
    
        account = self.find_account(to_withdraw_account)
    
        if not account:
            print("Account not found.\n")
            return 

        to_withdraw_balance = validate_positive_balance("Amount") 

        if account['balance'] >= to_withdraw_balance:
          account['balance'] -= to_withdraw_balance  
        else:
          print("Insufficient balance.")
          return
    
        print("\nAmount withdrawn successfully.")

        self.save_data()

    def transfer_money(self):

        clear_screen()
    
        if self.check_if_empty():
            return
        
        sender_account_no = validate_integer("Sender account No")
        sender_account = self.find_account(sender_account_no)
    
        if not sender_account:
            print("Sender account not found.\n")
            return
    
        receiver_account_no = validate_integer("Receiver account No")
        receiver_account = self.find_account(receiver_account_no)
    
        if not receiver_account:
            print("Receiver account not found.\n")
            return

        if sender_account == receiver_account:
            print("Sender and receiver cannot be same.\n")
            return

        to_transfer_balance = validate_positive_balance("Amount")


        if sender_account['balance'] >= to_transfer_balance:
          sender_account['balance'] -= to_transfer_balance
          receiver_account['balance'] += to_transfer_balance  
        else:
          print("Insufficient balance.")
          return
    
        print("\nAmount transferred successfully.")

        self.save_data()

    def delete_account(self):

        clear_screen()
    
        if self.check_if_empty():
            return
    
        to_delete = validate_integer("Account No")
    
        account = self.find_account(to_delete)

        if not account:
            print("Account not found.\n")
            return
    
        self.accounts.remove(account)
        self.save_data()
        print(f"\nAccount No {to_delete}, {account['name']} deleted successfully.")

    def save_data(self):

       with open("accountDetails.json", "w") as file:
          json.dump(self.accounts, file, indent=4)

    def load_data(self):
        try:
            with open("accountDetails.json", "r") as file:
                self.accounts = json.load(file)

        except FileNotFoundError:
                self.accounts = []

    def check_if_empty(self):

        if not self.accounts:
            print("No accounts available.\n")
            return True
        return False

accounts = BankSystem()

def show_menu():
    print("===================Banking System================\n")
    print("1. Create Account\n" \
        "2. View All Accounts\n" \
        "3. Search Account\n" \
        "4. Deposit Money\n" \
        "5. Withdraw Money\n" \
        "6. Transfer Money\n" \
        "7. Delete Account\n" \
        "8. Exit\n\n" \
        "Enter your choice: ")
    
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
                    accounts.create_account()
                case 2:
                    accounts.view_accounts()
                case 3:
                    accounts.search_account()
                case 4:
                    accounts.deposit_money()
                case 5:
                    accounts.withdraw_money()
                case 6:
                    accounts.transfer_money()
                case 7:
                    accounts.delete_account()
                case 8:
                    accounts.save_data()
                    sys.exit(0)
                case _:
                    print("Invalid Choice")

            input("\nPlease press enter to go back to the menu.")

main() 

