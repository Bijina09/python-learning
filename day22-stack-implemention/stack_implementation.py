import os
import sys

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

# Helper for checking empty input and integer
def validate_input(prompt):
    while True:
        try:
            while True:
                entered_value = input(f"{prompt} : ").strip()

                if not entered_value:
                    print(f"Input cannot be empty.\n")
                else:
                    break
            entered_number = int(entered_value)
            return entered_number
        except ValueError:
            print("Input must be an integer.\n")

def stack_empty():
    if not stack:
        print("Stack is empty.")
        print("Push an element first.")
        return True
    return False
    
stack = []

def push_element():

    clear_screen()

    to_push_element = validate_input("Enter element:")

    stack.append(to_push_element)
    print(f"\nPushed {to_push_element} successfully.")
  
def pop_element():

    clear_screen()

    if stack_empty():
        return

    print("Popped element: ", stack.pop())

def peek():

    clear_screen()

    if stack_empty():
        return

    print("Top of the stack :", stack[-1])

def display_stack():

    clear_screen()

    if stack_empty():
        return

    print("Stack from top to bottom.")
    for each_number in stack[::-1]:
        print(f"| {each_number} |")

    print("-----")
                
def check_if_stack_is_empty():

    clear_screen()

    if stack_empty():
        return
    else:
        print("Stack is not empty.")


def show_menu():
    print("===================Stack================\n")
    print("1. Push element\n" \
        "2. Pop element\n" \
        "3. Peek (Top element)\n" \
        "4. Display stack\n" \
        "5. Check if stack is empty\n" \
        "6. Exit\n\n" \
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
                    push_element()
                case 2:
                    pop_element()
                case 3:
                    peek()
                case 4:
                    display_stack()
                case 5:
                    check_if_stack_is_empty()
                case 6:
                    sys.exit(0)
                case _:
                    print("Invalid Choice")

            input("\nPlease press enter to go back to the menu.")

main()