import sys
import os

contacts = []

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

# Helper for displaying the question details
def display_contact_details(current_contact,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(f"\nName: {current_contact['name']}\n"
        f"Phone: {current_contact['phone']}\n"
        f"Email: {current_contact['email']}\n"
        f"Favorite: {favorite_status(current_contact['favorite'])}\n\n")

def validate_integer(prompt):
    while True:
        try:
            entered_value = int(check_if_empty_input(prompt))
            return entered_value
        except ValueError:
            print("Input must be an integer.")

def favorite_status(is_favorite):
    if is_favorite:
        return "Yes"
    else:
        return "No"

def validate_favorite(prompt):

    while True:

        entered_value = check_if_empty_input(prompt)

        if entered_value.lower() in ("y", "n"):
            if entered_value.lower() == "y":
                return True
            else:
                return False
        else:
   
            print("Please enter Y or N.\n")

def duplicate_check(prompt, contact=None):

    while True:
        duplicate_name = False

        entered_name = check_if_empty_input(prompt)

        for current_contact in contacts:
            if current_contact['name'].lower() == entered_name.lower():
                if contact is current_contact:
                    continue
               
                print("Contact already exists.\n")
                duplicate_name = True
                break

        if not duplicate_name:
            return entered_name

def add_contact():

    clear_screen()

    
    entered_name = duplicate_check("Name")
    entered_phone = validate_integer("Phone")
    entered_email = check_if_empty_input("Email")
    
    contact_details = {
        'name' : entered_name,
        'phone' : entered_phone,
        'email' : entered_email,
        'favorite' : False
    }

    contacts.append(contact_details)

def view_contacts():

    clear_screen()

    if not contacts:
        print("Contacts Not Available.\n")
        return

    for i, current_contact in enumerate(contacts, start=1):
        display_contact_details(current_contact, i)


def search_contact():

    clear_screen()

    if not contacts:
        print("Contacts Not Available.\n")
        return

    to_search = check_if_empty_input("Name")

    for contact_details in contacts:
        if contact_details['name'].lower() == to_search.lower():
            display_contact_details(contact_details)
            return
        
    print("\nContact Not Found.")

def update_contact():

    clear_screen()

    if not contacts:
        print("Contacts Not Available.\n")
        return

    to_update = check_if_empty_input("Name")

    for current_contact in contacts:
        if current_contact['name'].lower() == to_update.lower():
            current_contact['name'] = duplicate_check("\nNew Name",current_contact)
            current_contact['phone'] = validate_integer("New Phone")
            current_contact['email'] = check_if_empty_input("New Email")
            current_contact['favorite'] = validate_favorite("New Favorite Status (Y/N)")
            print("\nContact details updated successfully.")
            return
        
        
    print("\nContact Not Found.")

def delete_contact():

    clear_screen()

    if not contacts:
        print("Contacts Not Available.\n")
        return

    to_delete = check_if_empty_input("Name")

    for current_contact in contacts:
        if current_contact['name'].lower() == to_delete.lower():
            contacts.remove(current_contact)
            print(f"\nContact '{to_delete}' deleted successfully.")
            return
        
    print("\nContact Not Found.")

def toggle_favorite():

    clear_screen()

    if not contacts:
        print("Contacts Not Available.\n")
        return

    to_toggle = check_if_empty_input("Name")

    for current_contact in contacts:
        if current_contact['name'].lower() == to_toggle.lower():
            current_contact['favorite'] = not current_contact['favorite']
            if current_contact['favorite']:
                print("\nSuccessfully added to favorites.")
            else:
                print("\nSuccessfully removed from favorites.")
            return
        
    print("\nContact Not Found.")

def view_favorite_contacts():

    clear_screen()

    if not contacts:
        print("Contacts Not Available.\n")
        return

    i = 0
    for current_contact in contacts:
        if current_contact['favorite']:
            i += 1
            display_contact_details(current_contact,i)

    if i == 0:
        print("No favorite contacts.\n")

def show_menu():
    print("================Contact Book (Version 2)==============\n\n" \
    "1. Add Contact\n" \
    "2. View Contacts\n" \
    "3. Search Contact\n" \
    "4. Update Contact\n" \
    "5. Delete Contact\n" \
    "6. Toggle Favorite\n" \
    "7. View Favorite Contacts\n" \
    "8. Exit\n\n" \
    "Please enter your choice: ")


def main():

    while True:

        clear_screen()

        show_menu()

        try :
            choice = int(input())
        except ValueError:
            print("\nError: Please enter a valid integer\n")
            input("\nPress enter to continue")
        else:
            match choice:
                case 1:
                    add_contact()
                case 2:
                    view_contacts()
                case 3: 
                    search_contact()
                case 4:
                    update_contact()
                case 5:
                    delete_contact()
                case 6:
                    toggle_favorite()
                case 7:
                    view_favorite_contacts()
                case 8:
                    sys.exit(0)
                case _:
                    print("Please enter a valid choice.")

            input("\nPlease press enter to go to the menu.")


main()
