import sys
import os

# Function for clearing screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

products = []

# Helper Function for validating empty input

def check_if_empty_input(prompt):

    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print("Input cannot be empty.\n")
        else:
            return entered_value

def display_details(current_product, i=None):

    if i is not None:    
        print(f"\n{i}.")

    print(
        f"\nID : {current_product['id']}\n"
        f"Name : {current_product['name']}\n"
        f"Price : {current_product['price']}\n"
        f"Quantity : {current_product['quantity']}\n\n"
        )


def add_product():

    clear_screen()

    product_details = {}

    while True:

        duplicate_exists = False

        entered_productID = check_if_empty_input("Product ID")

        for current_product in products:
            if current_product['id'].lower() == entered_productID.lower():
                print("Product already exists.\n")
                duplicate_exists = True

        if not duplicate_exists:
            break

    entered_name = check_if_empty_input("Name")
    entered_price = int(check_if_empty_input("Price"))
    entered_quantity = int(check_if_empty_input("Quantity"))

    product_details = {
        'id' : entered_productID,
        'name' : entered_name,
        'price' : entered_price,
        'quantity' : entered_quantity
    }

    products.append(product_details)


def view_products():

    clear_screen()

    if not products:
        print("Products Not Available.\n")
        return

    for i, current_product in enumerate(products, start = 1):
        display_details(current_product, i)

def search_products():
     
    clear_screen()

    if not products:
        print("Products Not Available.\n")
        return
    
    to_search = check_if_empty_input("ID")

    for current_product in products:
        if current_product['id'].lower() == to_search.lower():
            display_details(current_product)
            return
        
    print("Product Not Found.\n")


def update_products():

    clear_screen()

    if not products:
        print("Products Not Available.\n")
        return
    
    to_update = check_if_empty_input("ID")

    for current_product in products:
        if current_product['id'].lower() == to_update.lower():
            new_name = check_if_empty_input("\nName")
            new_price = int(check_if_empty_input("Price"))
            new_quantity = int(check_if_empty_input("Quantity"))

            current_product['name'] = new_name
            current_product['price'] = new_price
            current_product['quantity'] = new_quantity
            print("\nProduct details updated successfully.")
            return
    
    print("Product Not Found.\n")


def delete_products():

    clear_screen()

    if not products:
        print("Products Not Available.\n")
        return
    
    to_delete = check_if_empty_input("ID")

    for current_product in products:
        if current_product['id'].lower() == to_delete.lower():
            products.remove(current_product)
            print("\nProduct deleted successfully.")
            return
        
    print("Product Not Found.")


def low_stock_report():

    clear_screen()

    if not products:
        print("Products Not Available.\n")
        return
    
    found = False
    print("Low Stock Products\n\n")
    for current_product in products:
        if current_product['quantity'] < 5:
            print(f"{current_product['name']} ({current_product['quantity']})")
            found = True

    if not found:
        print("No low stock products.")

def total_inventory_value():

    clear_screen()

    if not products:
        print("Products Not Available.\n")
        return
    
    total_inventory_value = 0

    for current_product in products:
        print(f"{current_product['name']}")
        print(f"{current_product['quantity']} * "\
              f"{current_product['price']} = "\
                f"{current_product['price'] * current_product['quantity']}\n")
        total_inventory_value += \
        current_product['price'] * current_product['quantity']

    print(f"Total Inventory Value = {total_inventory_value}")


# Menu
def show_menu():
    print("===================Inventory Management System================\n")
    print("1. Add Product\n" \
        "2. View Products\n" \
        "3. Search Product\n" \
        "4. Update Product\n" \
        "5. Delete Product\n"
        "6. Low Stock Report\n"
        "7. Total Inventory Value\n"
        "8. Exit\n\n" \
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
                    add_product()
                case 2:
                    view_products()
                case 3:
                    search_products()
                case 4:
                    update_products()
                case 5:
                    delete_products()
                case 6:
                    low_stock_report()
                case 7:
                    total_inventory_value() 
                case 8:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()