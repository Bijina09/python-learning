import os
import sys

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

def validate_input(prompt):
    while True:
        entered_value = input(prompt).strip()

        if not entered_value:
            print("Input cannot be empty.\n")
        else:
            return entered_value

class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class LinkedList:

    def __init__(self):
        self.head = None

    def add_node_at_the_end(self):

        clear_screen()

        data = validate_input("Enter data : ")
        new_node = Node(data)

        if self.check_if_list_is_empty():
            self.head = new_node
        else:
            current_node = self.head
            if not current_node.next:
                current_node.next = new_node
                new_node.prev = current_node
            else:
                while current_node.next:
                    current_node = current_node.next
                current_node.next = new_node
                new_node.prev = current_node

        print(f"\n'{data}' added successfully.")

    def add_node_at_the_beginning(self):

        clear_screen()

        data = validate_input("Enter data : ")
        new_node = Node(data)

        if self.check_if_list_is_empty():
            self.head = new_node
        else:
            current_node = self.head
            current_node.prev = new_node
            new_node.next = current_node
            self.head = new_node

        print(f"\nNew node '{new_node.data}' inserted successfully at the beginnning.\n")

    def display_list_forward(self):

        clear_screen()

        if self.check_if_list_is_empty():
            print("List is empty.")
            return

        current_node = self.head
        print("Head\n|\nV")
        print("None -> ",end="")
        while current_node:
            if not current_node.next:
                print(f"{current_node.data} -> ",end="")
                break
            print(f"{current_node.data} <-> ",end="")
            current_node = current_node.next

        print("None\n")

    def display_list_backward(self):
    
            clear_screen()
    
            if self.check_if_list_is_empty():
                print("List is empty.")
                return
    
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            print("Tail\n|\nV")
            print("None <- ",end="")
            while current_node:
                if not current_node.prev:
                    print(f"{current_node.data} -> ",end="")
                    break
                print(f"{current_node.data} <-> ",end="")
                current_node = current_node.prev
    
            print("None\n")

    def search_node(self):

        clear_screen()

        if self.check_if_list_is_empty():
            print("List is empty.")
            return

        to_search = validate_input("Enter the value to search : ")

        current_node = self.head

        while current_node:
            if current_node.data == to_search:
                print(f"\nData '{current_node.data}' found successfully.\n")
                return
            current_node = current_node.next

        print("\nData not found.\n")

    def delete_node(self):

        clear_screen()

        if self.check_if_list_is_empty():
            print("List is empty.")
            return

        to_delete = validate_input("Enter the data to delete : ")

        previous = None
        current_node = self.head
        
        while current_node: 
            if current_node.data == to_delete:
                if previous is None:
                    self.head = current_node.next
                    if current_node.next:
                        current_node.next.prev = None
                else:
                    previous.next = current_node.next
                    if current_node.next:
                        current_node.next.prev = current_node.prev
                print(f"\nData '{current_node.data}' deleted successfully.\n")
                return 
            previous = current_node
            current_node = current_node.next
                

        print(f"\nData '{to_delete}' not found.\n")

    def count_total_nodes(self):

        clear_screen()

        if self.check_if_list_is_empty():
            print("List is empty.")
            return

        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next

        print(f"\nTotal count is {count}.\n")

    # Helper function
    def check_if_list_is_empty(self):

        return self.head is None

    def display_list_status(self):

        clear_screen()

        if self.check_if_list_is_empty():
            print("List is empty.")
        else:
            print("List is not empty.")

    def clear(self):

        clear_screen()

        if self.check_if_list_is_empty():
            print("List is already empty.\n")
            return

        self.head = None
        print("\nList cleared successfully.\n")

linked_list = LinkedList()
    

def show_menu():
    print("===================Doubly Linked List================\n")
    print("1. Add node at the end\n" \
        "2. Add node at the beginning\n" \
        "3. Display linked list (forward)\n" \
        "4. Display linked list (backward)\n" \
        "5. Search node\n" \
        "6. Delete node\n" \
        "7. Count total nodes\n" \
        "8. Check if list is empty\n" \
        "9. Clear linked list\n" \
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
                    linked_list.add_node_at_the_end()
                case 2:
                    linked_list.add_node_at_the_beginning()
                case 3:
                    linked_list.display_list_forward()
                case 4:
                    linked_list.display_list_backward()
                case 5:
                    linked_list.search_node()
                case 6:
                    linked_list.delete_node()
                case 7:
                    linked_list.count_total_nodes()
                case 8:
                    linked_list.display_list_status()
                case 9:
                    linked_list.clear()
                case 10:
                    sys.exit(0)
                case _:
                    print("Invalid Choice")

            input("\nPlease press enter to go back to the menu.")

main()  