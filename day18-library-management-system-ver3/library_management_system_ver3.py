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

def return_available_status(is_available):

    return 'Yes' if is_available else 'No'
         
# Helper for displaying the book details
def display_book_details(current_book,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"\nBook ID : {current_book['book_id']}\n"
    f"Title : {current_book['title']}\n"
    f"Author : {current_book['author']}\n"
    f"Category : {current_book['category']}\n"
    f"Price :  Rs. {current_book['price']:.2f}\n"
    f"Available : {return_available_status(current_book['available'])}\n")

# Helper for displaying the book details
def display_category_details(current_category,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"\nCategory : {current_category['name']}\n"
    f"Count : {current_category['count']}\n")

def validate_integer(prompt):
    while True:
        try:
            entered_value = int(check_if_empty_input(prompt))
            return entered_value
        except ValueError:
            print("Input must be an integer.\n")

# Helper for checking empty input
def check_positive(prompt):
    while True:
        entered_value = validate_integer(prompt)

        if entered_value <= 0:
            print(f"Price must be greater than 0.\n")
        else:
            return entered_value
        
def duplicate_book_check(prompt, book=None):

    while True:
        duplicate_exists = False

        entered_book_id = validate_integer(prompt)

        for current_book in books:
            if current_book['book_id'] == entered_book_id:
                if current_book is book:
                    continue
                print("Book already exists.\n")
                duplicate_exists = True
                break

        if not duplicate_exists:
            return entered_book_id

def find_book(book_id):

    for current_book in books:
        if current_book['book_id'] == book_id:
            return current_book

    return None    

def validate_available_status(prompt):

    while True:

        status = check_if_empty_input(prompt)

        if status.lower() == 'n':
            return False
        elif status.lower() == 'y':
            return True 
        
        print("Please enter Y/N.")
                
# Function for adding book
def add_book():

    clear_screen()

    entered_book_id = duplicate_book_check("Book ID")
    entered_title = check_if_empty_input("Title")
    entered_author = check_if_empty_input("Author")
    entered_category = check_if_empty_input("Category")
    entered_price = check_positive("Price")

    book_details = {
        'book_id' : entered_book_id,
        'title' : entered_title,
        'author' : entered_author,
        'category' : entered_category,
        'price' : entered_price,
        'available' : True
    }

    books.append(book_details)
    print("\nBook added successfully.\n")

# View all Books function
def view_all_books():

    clear_screen()

    if not books:
        print("No Books Available.\n")
        return
    
    print("Book Details")
    for i, current_book in enumerate(books, start=1):
        display_book_details(current_book,i=i)

# Function for searching book
def search_book():

    clear_screen()

    if not books:
        print("No Books Available.\n")
        return
    
    to_search = validate_integer("Book ID")

    book = find_book(to_search)

    if book is None:
        print("\nBook Not Found.\n")
        return

    display_book_details(book)
    

def update_book_details():

    clear_screen()

    if not books:
        print("No Books Available.\n")
        return
    
    to_update_book = validate_integer("Book ID")

    book = find_book(to_update_book)

    if book is None:
        print("\nBook Not Found.\n")
        return

    book['book_id'] = duplicate_book_check("New Book ID",book)
    book['title'] = check_if_empty_input("New Title")
    book['author'] = check_if_empty_input("New Author")
    book['category'] = check_if_empty_input("New Category")
    book['price'] = check_positive("New Price")

    print(f"\nBook details updated successfully.")

def delete_book():

    clear_screen()

    if not books:
        print("No Books Available.\n")
        return

    to_delete = validate_integer("Book ID")

    book = find_book(to_delete)
    if book is None:
        print("\nBook Not Found.\n")
        return

    if book['available']:
        books.remove(book)
        print(f"\nBook ID {to_delete}, {book['title']} deleted successfully.")
        return
    else:
        print("Cannot delete.\nBook is currently borrowed.\n")

def borrow_book():

    clear_screen()

    if not books:
        print("No Books Available.\n")
        return

    to_borrow = validate_integer('Book ID')

    book = find_book(to_borrow)

    if book is None:
        print("\nBook Not Found.\n")
        return
    
    if book['available']:
        book['available'] = False
        print(f"Book '{book['title']}' borrowed successfully.\n")
    else:
        print("Book not available for borrowing.\n")


def return_book():

    clear_screen()

    if not books:
        print("No Books Available.\n")
        return

    to_return = validate_integer('Book ID')

    book = find_book(to_return)

    if book is None:
        print("\nBook Not Found.\n")
        return
    
    if not book['available']:
        book['available'] = True
        print(f"Book '{book['title']}' has been returned successfully.\n")
    else:
        print("Book not borrowed.\n")

def view_available_books():

    clear_screen()

    if not books:
        print("No Books Available.\n")
        return

    print("Available Books:\n")
    i = 0
    for current_book in books:
        if current_book['available']:
            i += 1
            display_book_details(current_book, i)
    
    if i == 0:
        print(f"No Books Currently Available.")

def view_borrowed_books():

    clear_screen()

    if not books:
        print("No Books Available.\n")
        return

    print("Borrowed Books:\n")
    i = 0
    for current_book in books:
        if not current_book['available']:
            i += 1
            display_book_details(current_book, i)
    
    if i == 0:
        print(f"No Books Currently Borrowed.")

def display_most_expensive_books():
    
    clear_screen()

    if not books:
        print("No Books Available.\n")
        return

    highest_price = books[0]['price']

    for current_book in books:
        if current_book['price'] > highest_price:
            highest_price = current_book['price']

    print("Most Expensive Book(s):")
    i = 0
    for current_book in books:
        if current_book['price'] == highest_price:
            i += 1
            display_book_details(current_book, i)

def count_books_by_category():

    clear_screen()

    if not books:
        print("No Books Available.\n")
        return
    
    categories = []

    for current_book in books:
        duplicate = False
        for current_category in categories:
            if current_book['category'].lower() == current_category['name'].lower():
                duplicate = True
                break
            
        if not duplicate:
            categories.append({
                'name' : current_book['category']
            })


    for current_book in books:
        for current_category in categories:
            if current_book['category'].lower() == current_category['name'].lower():
                if 'count' not in current_category:
                    current_category['count'] = 0
                current_category['count'] += 1
                break
    
    print("Book Categories:")
    for i, current_category in enumerate(categories, start=1):
        display_category_details(current_category, i)

    
def show_menu():
    print("===================Library Management System (Version 3)================\n")
    print("1. Add Book\n" \
        "2. View All Books\n" \
        "3. Search Book\n" \
        "4. Update Book Details\n" \
        "5. Delete Book\n"
        "6. Borrow Book\n"
        "7. Return Book\n"
        "8. View Available Books\n"
        "9. View Borrowed Books\n"
        "10. Display Most Expensive Book(s)\n"
        "11. Count Books By Category\n"
        "12. Exit\n\n" \
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
                    search_book()
                case 4:
                    update_book_details()
                case 5:
                    delete_book()
                case 6:
                    borrow_book()
                case 7:
                    return_book()
                case 8:
                    view_available_books()
                case 9:
                    view_borrowed_books() 
                case 10:
                    display_most_expensive_books()
                case 11:
                    count_books_by_category()  
                case 12:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()