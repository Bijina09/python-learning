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
                
numbers_list = []

def enter_numbers():

    clear_screen()

    numbers_list.clear()

    entered_numbers = input("Enter numbers separated by spaces: ")

    string_numbers_list = entered_numbers.split()
    for each_number in string_numbers_list:
        numbers_list.append(int(each_number))
  
def display_numbers():

    clear_screen()

    if not numbers_list:
        print("No numbers present.")
        print("Enter numbers first.")
        return

    print("Numbers:")
    for each_number in numbers_list:
        print(f"{each_number} ",end="")

def linear_search():

    clear_screen()

    if not numbers_list:
            print("No numbers present.")
            print("Enter numbers first.")
            return
    
    to_search = validate_input("Enter number to search: ")

    for index, each_number in enumerate(numbers_list):
        if each_number == to_search:
            print(f"Number found at index {index}.\n")
            print(f"Comparisons : {index+1}")
            return

    print("Number not found.")

def binary_search():

    clear_screen()

    if not numbers_list:
        print("No numbers present.")
        print("Enter numbers first.")
        return

    to_search = validate_input("Enter number to search: ")

    numbers = numbers_list[:]
    
    print(f"Original Array: ")
    print(numbers)

    length = len(numbers)

    for i in range(1, length):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j = j - 1
        numbers[j + 1] = key

    print("Sorted array: ", numbers)

    left = 0
    right = length - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if numbers[mid] == to_search:
            print(f"Number found at index {mid}.")
            print(f"Comparisons : {comparisons}")
            return
        elif numbers[mid] > to_search:
            right = mid - 1
        else:
            left = mid + 1

    print("Number not found.")

def show_menu():
    print("===================Searching Algorithms================\n")
    print("1. Enter Numbers\n" \
        "2. Display Numbers\n" \
        "3. Linear Search\n" \
        "4. Binary Search\n" \
        "5. Exit\n\n" \
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
                    enter_numbers()
                case 2:
                    display_numbers()
                case 3:
                    linear_search()
                case 4:
                    binary_search()
                case 5:
                    sys.exit(0)
                case _:
                    print("Invalid Choice")

            input("\nPlease press enter to go back to the menu.")

main()