import os
import sys

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")
    
def left_triangle():
    clear_screen()
    for i in range(6):
        for j in range(i):
            print("*",end="")

        print("\n")

def upside_down_triangle():
    clear_screen()
    for i in range(5,0,-1):
        for j in range(i):
            print("*", end="")

        print("\n")
def central_equilateral_triangle():
    clear_screen()

    n = 4
    for i in range(n):
        for space in range(n-i-1):
            print(" ",end="")
        for star in range(i+(i+1)):
            print("*",end="")
        print()




def show_menu():
    print("===================Pattern Printing================\n")
    print("1. Left Sided Triangle\n" \
        "2. Upside Down Triangle\n" \
        "3. Central Equilateral Triangle\n" \
        "4. Exit\n\n" \
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
                    left_triangle()
                case 2:
                    upside_down_triangle()
                case 3:
                    central_equilateral_triangle()
                case 4:
                    sys.exit(0)
                case _:
                    print("Invalid Choice")

            input("\nPlease press enter to go back to the menu.\n")

main()