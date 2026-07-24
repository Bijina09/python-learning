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

def queue_empty():
    if not queue:
        print("Queue is empty.")
        print("Enqueue an element first.")
        return True
    return False
    
queue = []

def enqueue_element():

    clear_screen()

    to_enqueue_element = validate_input("Enter element:")

    queue.append(to_enqueue_element)
    print(f"\nEnqueued {to_enqueue_element} successfully.")
  
def dequeue_element():

    clear_screen()

    if queue_empty():
        return

    print("Dequeued element: ", queue.pop(0))

def peek():

    clear_screen()

    if queue_empty():
        return

    print("Front of the queue :", queue[0])

def display_queue():

    clear_screen()

    if queue_empty():
        return

    print("Queue:")
    print("Front ->", end="")
    for each_number in queue:
        print(f"| {each_number} | ", end="")

    print("<- Rear")          
def check_if_queue_is_empty():

    clear_screen()

    if queue_empty():
        return
    else:
        print("Queue is not empty.")

def display_queue_size():

    clear_screen()

    print(f"Queue size: {len(queue)}")

def peek_both_ends():

    clear_screen()
    
    if queue_empty():
        return
    
    print("Front of the queue :", queue[0])
    print("Rear of the queue :", queue[-1])

def clear_queue():

    clear_screen()

    if queue_empty():
        return

    queue.clear()
    print("Queue cleared successfully.")

def search_element():

    clear_screen()

    if queue_empty():
        return

    to_search_element = validate_input("Enter number:")

    for i, current_element in enumerate(queue):
        if current_element == to_search_element:
            print(f"Element {to_search_element} found in the queue at position {i}.")
            return

    print(f"Element {to_search_element} not found")
    

def show_menu():
    print("===================Queue================\n")
    print("1. Enqueue element\n" \
        "2. Dequeue element\n" \
        "3. Peek (Front element)\n" \
        "4. Display queue\n" \
        "5. Check if queue is empty\n" \
        "6. Display queue size\n" \
        "7. Peek both ends\n" \
        "8. Clear queue\n" \
        "9. Search element\n" \
        "10. Exit\n\n" \
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
                    enqueue_element()
                case 2:
                    dequeue_element()
                case 3:
                    peek()
                case 4:
                    display_queue()
                case 5:
                    check_if_queue_is_empty()
                case 6:
                    display_queue_size()
                case 7:
                    peek_both_ends()
                case 8:
                    clear_queue()
                case 9:
                    search_element()
                case 10:
                    sys.exit(0)
                case _:
                    print("Invalid Choice")

            input("\nPlease press enter to go back to the menu.")

main()