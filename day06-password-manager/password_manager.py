import sys
import getpass

accounts = []

def clear_screen():
    print("\033[H\033[J", end="")

def check_if_empty_input(prompt, hidden=False):
    while True:
        if hidden:
            entered_value = getpass.getpass(f"{prompt} : ").strip()    
        else:
            entered_value = input(f"{prompt} : ").strip()
        if not entered_value:
            print("\nError: Input cannot be empty.\n")
        else:
            return entered_value

def add_account():

    clear_screen()

    account_details = {}

    while True:
        duplicate_exists = False
        
        entered_website = check_if_empty_input("Website")

        entered_username = check_if_empty_input("Username")

        for current_account in accounts:
            if (current_account['website'].lower() == entered_website.lower()
            and
            current_account['username'].lower() == entered_username.lower()):
                print("\nAccount already exists\n")
                duplicate_exists = True
                break

        if not duplicate_exists:
            break
    
    account_details['website'] = entered_website
    account_details['username'] = entered_username

    while True:

        entered_password = check_if_empty_input("Password", hidden=True)

        if len(entered_password) < 8:
            print("Password length should be atleast 8.")
        else:
            break

    account_details['password'] = entered_password
    accounts.append(account_details)

def view_accounts():

    clear_screen()

    if not accounts:
        print("\nNo Accounts Available.")
        return
    
    for i, current_account in enumerate(accounts):
        print(f"{i+1}.\n"
              f"Website : {current_account['website']}\n"
              f"Username : {current_account['username']}\n"
              "Password : ********\n\n")

def search_website():

    clear_screen()
    
    if not accounts:
        print("\nNo Accounts Available")
        return

    to_search = check_if_empty_input("Website")

    search_found = False
    searched_accounts = []

    for current_account in accounts:
        if current_account['website'].lower() == to_search.lower():
            search_found = True
            searched_accounts.append(current_account)
            print(f"\n\nWebsite: {current_account['website']}\n"
                f"Username : {current_account['username']}\n")

    if not search_found:   
        print("\nNo Account Found.")
        return

    while True:

        reveal_password = check_if_empty_input("Reveal Password? (y/n)")
            
        if (reveal_password.lower()) == 'y':
            for current_account in searched_accounts:
                print(f"\nUsername : {current_account['username']}")
                print(f"Password : {current_account['password']}\n")
            break
        elif (reveal_password.lower()) == 'n':
            break
        else:
            print("\nPlease enter y/n.")
            
                      
def delete_account():

    clear_screen()

    if not accounts:
        print("\nNo Accounts Available.")
        return

    to_delete_website = check_if_empty_input("Website")
    to_delete_username = check_if_empty_input("Username")

    for current_account in accounts:
        if (current_account['website'].lower() == to_delete_website.lower() 
        and 
        current_account['username'].lower() == to_delete_username.lower()):
            accounts.remove(current_account)
            print("Account Deleted Successfully.")
            return
        
    print("\nNo Account Found.")



def show_menu():
    print("===================Password Manager================\n\n")
    print("1. Add Account\n" \
        "2. View Accounts\n" \
        "3. Search Website\n" \
        "4. Delete Account\n" \
        "5. Exit\n\n" \
        "Enter your choice: ")
    
def main():

    while True:

        clear_screen ()

        show_menu()

        try:
            choice = int(input())
        except ValueError:
            print("\nError: Please enter a valid integer\n")
            input("\nPress enter to continue")
        else:
            match choice:
                case 1:
                    add_account()
                case 2:
                    view_accounts()
                case 3:
                    search_website()
                case 4:
                    delete_account()
                case 5:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()