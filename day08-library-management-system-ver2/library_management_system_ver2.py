import sys
import os

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

books = []

# Helper for checking empty input
def check_if_empty_input(prompt):
    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print(f"Input cannot be empty.\n")
        else:
            return entered_value

# Helper for returning status for boolean value
def return_status(status):
    if status:
        return 'Available'
    else:
        return 'Borrowed'

# Helper for displaying the book details
def display_book_details(current_book,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"Title : {current_book['title']}\n"
    f"Author : {current_book['author']}\n"
    f"Status : {return_status(current_book['available'])}\n")

    
# Add Book Function
def add_book():
    
    clear_screen()

    book_details = {}

    while True:
        duplicate_exists = False

        entered_title = check_if_empty_input("Title")
        entered_author = check_if_empty_input('Author')

        for current_book in books:
            if (current_book['title'].lower() == entered_title.lower()
            and current_book['author'].lower() == entered_author.lower()):
                print("Book already exists.\n")
                duplicate_exists = True
                break
        
        if not duplicate_exists:
            break

    book_details = {
        'title' : entered_title,
        'author' : entered_author,
        'available' : True
    }

    books.append(book_details)

# View all Books function
def view_all_books():

    clear_screen()

    if not books:
        print("No Books Available.\n")
        return
    
    print("Book Details")
    for i, current_book in enumerate(books, start=1):
        display_book_details(current_book,i=i)

# Search book by title function
def search_book_by_title():

    clear_screen()

    if not books:
        print("Books Not Available.\n")
        return

    title_to_search = check_if_empty_input("Title")

    for current_book in books:
        if current_book['title'].lower() == title_to_search.lower():
            display_book_details(current_book)
            return
    
    print("Book Not Found.\n")

# Function for borrowing book
def borrow_book():

    clear_screen()

    if not books:
        print("Books Not Available.\n")
        return

    to_borrow = check_if_empty_input("Title")

    for current_book in books:
        if current_book['title'].lower() == to_borrow.lower():
            if not current_book['available']:
                print("Book has already been borrowed.\n")
                return
            else:
                current_book['available'] = False
                print("Book borrowed successfully.\n")
                return
        
    print("Book Not Found.\n")

#Function for returning book
def return_book():

    clear_screen()

    if not books:
        print("Books Not Available.\n")
        return

    to_return = check_if_empty_input('Title')


    for current_book in books:
        if current_book['title'].lower() == to_return.lower():
            if current_book['available']:
                print("Book has not been borrowed.\n")
                return
            else:
                current_book['available'] = True
                print("Book returned successfully.\n")
                return
        
    print("Book Not Found.\n")

# Function for viewing borrowed books
def view_borrowed_books():

    clear_screen()

    if not books:
        print("Books Not Available.\n")
        return
    
    print("Borrowed books.\n\n")

    found = False
    i = 0
    for current_book in books: 
        if not current_book['available']:
            found = True
            i+=1
            display_book_details(current_book,i)
    
    if not found:
        print("No borrowed books.")

# FUnction for viewing available books        
def view_available_books():

    clear_screen()

    if not books:
        print("Books Not Available.\n")
        return
    
    print("Available Books\n\n")

    found = False
    i = 0
    for current_book in books:  
        if current_book['available']:
            found = True
            i+=1
            display_book_details(current_book,i)

    if not found:
        print("No available books.")

# Function for deleting a book
def delete_book():

    clear_screen()

    if not books:
        print("Books Not Available.\n")
        return
    
    to_delete = check_if_empty_input("Title")

    for current_book in books:
        if current_book['title'].lower() == to_delete.lower():
            books.remove(current_book)
            print("Book deleted successfully.\n")
            return
        
    print("Book Not Found.\n")

# Menu
def show_menu():
    print("===================Library Management System Ver 2================\n\n")
    print("1. Add a Book\n" \
        "2. View All Books\n" \
        "3. Search Book by Title\n" \
        "4. Borrow a Book\n" \
        "5. Return a Book\n"
        "6. View Borrowed Books\n"
        "7. View Available Books\n"
        "8. Delete a Book\n"
        "9. Exit\n\n" \
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
                    add_book()
                case 2:
                    view_all_books()
                case 3:
                    search_book_by_title()
                case 4:
                    borrow_book()
                case 5:
                    return_book()
                case 6:
                    view_borrowed_books()
                case 7:
                    view_available_books() 
                case 8:
                    delete_book()
                case 9:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()