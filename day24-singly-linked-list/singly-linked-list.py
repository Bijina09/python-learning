import os
import sys

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:

    def __init__(self):
        self.head = None

    def add_node_at_the_end(self):

        clear_screen()

        data = input("Enter data: ").strip()
        new_node = Node(data)

        if self.check_if_list_is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node


    def display_linked_list(self):

        if self.check_if_list_is_empty():
            return

        current_node = self.head

        while current_node is not None:
            if current_node.next is not None:
                print(f"Data : {current_node.data} ->",end="")
            else:
                print(f"Data : {current_node.data} -> None",end="")
            current_node = current_node.next


    def search_node(self):

        clear_screen()

        if self.check_if_list_is_empty():
            return

        to_search = input("Enter the value to search: ").strip()

        current_node = self.head

        while current_node is not None:
            if current_node.data == to_search:
                print(f"Data {current_node.data}found successfully.\n")
                return
            current_node = current_node.next

        print("Data not found.\n")

    def delete_node(self):

        clear_screen()

        if self.check_if_list_is_empty():
            return

        to_delete = input("Enter the value to delete: ").strip()

        previous = None
        current_node = self.head
        
        while current_node is not None: 
            if current_node.data == to_delete:
                if previous is None:
                    self.head = None
                else:
                    previous.next = current_node.next  
            else:
                previous = current_node
                current_node = current_node.next
                print(f"Data {current_node.data} deleted successfully.\n")
                return
            current_node = current_node.next

        print(f"Data {to_delete} not found.\n")
    def count_total_nodes(self):

        clear_screen()

        if self.check_if_list_is_empty():
            return

        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next

        print(f"Total count is {count}.\n")

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
        print("List cleared successfully.\n")

linked_list = LinkedList()
    

def show_menu():
    print("===================Singly Linked List================\n")
    print("1. Add node at the end\n" \
        "2. Display linked list\n" \
        "3. Search node\n" \
        "4. Delete node\n" \
        "5. Count total nodes\n" \
        "6. Check if list is empty\n" \
        "7. Clear linked list\n" \
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
                    linked_list.add_node_at_the_end()
                case 2:
                    linked_list.display_linked_list()
                case 3:
                    linked_list.search_node()
                case 4:
                    linked_list.delete_node()
                case 5:
                    linked_list.count_total_nodes()
                case 6:
                    linked_list.display_list_status()
                case 7:
                    linked_list.clear()
                case 8:
                    sys.exit(0)
                case _:
                    print("Invalid Choice")

            input("\nPlease press enter to go back to the menu.")

main()  