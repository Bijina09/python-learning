import sys

contact = []

def clear_screen():
    print("\033[H\033[J", end="")

def add_contact():

    clear_screen()

    contact_details = {}

    while True:
        duplicate_name = False

        print("Please enter the name: ")
        entered_name = input()

        for current_contact in contact:
            if current_contact['name'].lower() == entered_name.lower():
                print("Contact already exists.\n")
                duplicate_name = True
                break

        if not duplicate_name:
            break

    
    contact_details['name'] = entered_name

    print("Please enter the number: ")
    contact_details['phone'] = input()

    print("Please enter the email: ")
    contact_details['email'] = input()

    contact.append(contact_details)

def view_contact():

    clear_screen()

    for i, contact_details in enumerate(contact):
        print(f"{i+1}.\n"
            f"Name: {contact_details['name']}\n"
            f"Phone: {contact_details['phone']}\n"
            f"Email: {contact_details['email']}\n\n")


def search_contact():

    clear_screen()

    print("Please enter the contact name to search: ")
    to_search = input()

    for contact_details in contact:
        if contact_details['name'].lower() == to_search.lower():
            print("\nContact Found.\n\n" \
            f"Name: {contact_details['name']}\n"
            f"Phone: {contact_details['phone']}\n"
            f"Email: {contact_details['email']}")

            return
        
    print("\nContact Not Found.")


def delete_contact():

    clear_screen()

    print("Enter the name of the contact to delete: ")
    to_delete = input()

    for contact_details in contact:
        if contact_details['name'].lower() == to_delete.lower():
            contact.remove(contact_details)

            print(f"Contact {to_delete} deleted successfully.")

            return
        
    print("\nContact Not Found.")

def show_menu():
    print("================Contact Book==============\n\n" \
    "1. Add Contact\n" \
    "2. View Contact\n" \
    "3. Search Contact\n" \
    "4. Delete Contact\n" \
    "5. Exit\n\n" \
    "Please enter your choice: ")


def main():

    while True:

        clear_screen()

        show_menu()

        choice = int(input())

        match choice:
            case 1:
                add_contact()
            case 2:
                view_contact()
            case 3: 
                search_contact()
            case 4:
                delete_contact()
            case 5:
                sys.exit(0)
            case _:
                print("Please enter a valid choice.")

        print("\nPlease press enter to go to the menu.")

        input()


main()
