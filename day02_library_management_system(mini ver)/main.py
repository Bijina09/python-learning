import sys

book = []

def clear_screen():
    print("\033[H\033[J", end="")

# Adds book
def add_book():

    clear_screen()

    book_details = {}

    while True: 

        duplicate_book_found = False

        print("Enter the book title: ")
        entered_book_title = input()

        for current_book in book:
            if(current_book['title'].lower() == entered_book_title.lower()):
                print("Book already exits.\n")
                duplicate_book_found = True
                break

        if not duplicate_book_found:
            break

    book_details['title'] = entered_book_title

    print("Enter the author name: ")
    book_details['author'] = input()

    book.append(book_details)

# Displays all the books
def view_books():

    clear_screen()

    for i, current_book in enumerate(book):
        print(f"{i+1}\n" \
            f"Title: {current_book['title']}\n"
            f"Author: {current_book['author']}\n\n"
        )

def search_book():

    clear_screen()

    print("Enter title: ")
    to_search_title = input().lower()

    for current_book in book:
        if current_book['title'].lower() == to_search_title:
            print("\nBook Found\n" 
                f"Title: {current_book['title']}\n"
                f"Author: {current_book['author']}\n"
            )
            
            return

    print("Book not found.")



def show_menu():
    print("==========================Library Menu===========================\n\n")
    print("1. Add Book\n" \
            "2. View Books\n" \
            "3. Search Book\n" \
            "4. Exit\n\n" \
            "Enter your choice: ")

def main():
    
    while True:
        clear_screen()
        show_menu()
        
        choice = int(input())

        match choice:
            case 1:
                add_book()
            case 2:
                view_books()
            case 3:
                search_book()
            case 4:
                sys.exit(0)
            case _:
                print("Invalid choice")

        input("\nPress Enter to return to the menu.")


main()