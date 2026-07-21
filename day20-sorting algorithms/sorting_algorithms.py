import os
import sys

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")
    
original_numbers = []
def enter_numbers():

    clear_screen()

    entered_numbers = input("Enter numbers separated by spaces: ")

    numbers_list = entered_numbers.split()
    for each_number in numbers_list:
        original_numbers.append(int(each_number))
  

def bubble_sort():

    clear_screen()

    if not original_numbers:
        print("Enter numbers first.")
        return

    numbers = original_numbers[:]
    
    length = len(numbers)
    
    print(f"Original Array: ")
    print(numbers)
    stop = length - 1 
    for i in range(length - 1):
        for j in range(stop):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
            
        stop = stop - 1
 
    print("sorted array : ")
    print(numbers)

def selection_sort():
    clear_screen()

    if not original_numbers:
        print("Enter numbers first.")
        return
    
    numbers = original_numbers[:]

    print(f"Original Array: ")
    print(numbers)

    length = len(numbers)

    for i in range(length - 1):
        min_index = i
        for j in range(i+1,length):
            if numbers[j] < numbers[min_index]:
                min_index = j

        temp = numbers[i]
        numbers[i] = numbers[min_index]
        numbers[min_index] = temp

    
    print("Sorted array : ")
    print(numbers)

def insertion_sort():

    clear_screen()

    if not original_numbers:
        print("Enter numbers first.")
        return
    
    numbers = original_numbers[:]
    
    print(f"Original Array: ")
    print(numbers)

    length = len(numbers)
    start = numbers[0]

    for i in range(1, length):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j = j - 1
        numbers[j+1] = key

    print("Sorted array : ")
    print(numbers)


def show_menu():
    print("===================Sorting Algorithm================\n")
    print("1. Enter numbers\n" \
        "2. Bubble sort\n" \
        "3. Selection sort\n" \
        "4. Insertion sort\n" \
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
                    bubble_sort()
                case 3:
                    selection_sort()
                case 4:
                    insertion_sort()
                case 5:
                    sys.exit(0)
                case _:
                    print("Invalid Choice")

            input("\nPlease press enter to go back to the menu.\n")

main()