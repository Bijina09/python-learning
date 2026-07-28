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

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Tree:

    def __init__(self):
        self.root = None

    def insert_node(self):

        clear_screen()

        entered_value = validate_input("Enter value : ")
        new_node = Node(entered_value)

        if self.check_if_empty_tree():
            self.root = new_node
            print("Node inserted successfully.\n")
            return
        else:
            insert_status = self.insert_new_node(self.root,entered_value,new_node)

            if insert_status:
                print("Node inserted successfully.\n")
            else:
                print(f"Entered value '{entered_value}' already exists.\n")

    def insert_new_node(self,node,entered_value,new_node):
        current_node = node
        if entered_value == current_node.value:             
            return False
        if entered_value > current_node.value:
            if not current_node.right:             
                current_node.right = new_node
                return True
            return self.insert_new_node(current_node.right,entered_value,new_node)
        elif entered_value < current_node.value: 
            if not current_node.left:
                current_node.left = new_node
                return True
            return self.insert_new_node(current_node.left,entered_value,new_node)

    def search_node(self):

        clear_screen()

        if not tree.root:
            print("Tree is empty.\n")
            return

        to_search = validate_input("Enter value : ")

        current_node = self.root

        search_result = self.search_each_node(current_node,to_search)

        if search_result:
            print(f"Value '{to_search}' found in the tree.\n")
            return
        else:
            print(f"Value '{to_search}' not found in the tree.\n")
            return

    def search_each_node(self,current_node,to_search):     
        if current_node:
            if current_node.value == to_search:
                return True
            elif to_search > current_node.value:
                if current_node.right:
                    return self.search_each_node(current_node.right,to_search)
                else:
                    return False
            else:
                if current_node.left:
                    return self.search_each_node(current_node.left,to_search)
                else:
                    return False
        else:
            return False

    def inorder_traversal(self):

        clear_screen()

        if not tree.root:
            print("Tree is empty.\n")
            return

        current_node = tree.root

        self.each_inorder(current_node)

    def each_inorder(self, current_node):
        if not current_node:
            return

        self.each_inorder(current_node.left)
        print(f"{current_node.value} -> ",end="")
        self.each_inorder(current_node.right)

    
    def preorder_traversal(self):
    
        clear_screen()
            
        if not tree.root:
            print("Tree is empty.\n")
            return
            
        current_node = tree.root
            
        self.each_preorder(current_node)
            
    def each_preorder(self, current_node):
        if not current_node:
            return
            
        print(f"{current_node.value} -> ",end="")
        self.each_preorder(current_node.left)
        self.each_preorder(current_node.right)
        

    def postorder_traversal(self):

        clear_screen()
                    
        if not tree.root:
            print("Tree is empty.\n")
            return
            
        current_node = tree.root
                    
        self.each_postorder(current_node)
                    
    def each_postorder(self, current_node):
        if not current_node:
            return
                    
        self.each_postorder(current_node.left)
        self.each_postorder(current_node.right)
        print(f"{current_node.value } -> ",end="")

    def find_minimum(self):

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

    def find_maximum(self):

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
    def check_if_empty_tree(self):

        return self.root is None

    def count_total_nodes(self):

        clear_screen()

        if self.check_if_list_is_empty():
            print("List is empty.")
        else:
            print("List is not empty.")

tree = Tree()

def show_menu():
    print("===================Binary Search Tree================\n")
    print("1. Insert node\n" \
        "2. Search node\n" \
        "3. Inorder traversal\n" \
        "4. Preorder traversal\n" \
        "5. Postorder traversal\n" \
        "6. Find minimum\n" \
        "7. Find maximum\n" \
        "8. Count total nodes\n" \
        "9. Exit\n\n" \
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
                    tree.insert_node()
                case 2:
                    tree.search_node()
                case 3:
                    tree.inorder_traversal()
                case 4:
                    tree.preorder_traversal()
                case 5:
                    tree.postorder_traversal()
                case 6:
                    tree.find_minimum()
                case 7:
                    tree.find_maximum()
                case 8:
                    tree.count_total_nodes()
                case 9:
                    sys.exit(0)
                case _:
                    print("Invalid Choice")

            input("\nPlease press enter to go back to the menu.")

main()  