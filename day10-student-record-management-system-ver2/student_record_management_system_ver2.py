import sys
import os

# Function for clearing screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

students = []

# Helper Function for validating empty input

def check_if_empty_input(prompt):

    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print("Input cannot be empty.\n")
        else:
            return entered_value

def display_details(current_student, i=None):

    if i is not None:    
        print(f"\n{i}.")

    print(
        f"\nID : {current_student['id']}\n"
        f"Name : {current_student['name']}\n"
        f"Age : {current_student['age']}\n"
        f"Marks : {current_student['marks']}\n\n"
        )


def add_student():

    clear_screen()

    student_details = {}

    while True:

        duplicate_exists = False

        entered_id = check_if_empty_input("ID")

        for current_student in students:
            if current_student['id'].lower() == entered_id.lower():
                print("Student already exists.\n")
                duplicate_exists = True

        if not duplicate_exists:
            break

    entered_name = check_if_empty_input("Name")
    entered_age = int(check_if_empty_input("Age"))
    entered_marks = int(check_if_empty_input("Marks"))

    student_details = {
        'id' : entered_id,
        'name' : entered_name,
        'age' : entered_age,
        'marks' : entered_marks
    }

    students.append(student_details)


def view_students():

    clear_screen()

    if not students:
        print("Students Not Available.\n")
        return

    for i, current_student in enumerate(students, start = 1):
        display_details(current_student, i)

def search_students():
     
    clear_screen()

    if not students:
        print("Students Not Available.\n")
        return
    
    to_search = check_if_empty_input("ID")

    for current_student in students:
        if current_student['id'].lower() == to_search.lower():
            display_details(current_student)
            return
        
    print("Student Not Found.\n")


def update_student():

    clear_screen()

    if not students:
        print("Students Not Available.\n")
        return
    
    to_update = check_if_empty_input("ID")

    for current_student in students:
        if current_student['id'].lower() == to_update.lower():
            new_name = check_if_empty_input("\nName")
            new_age = int(check_if_empty_input("Age"))
            new_marks = int(check_if_empty_input("Marks"))

            current_student['name'] = new_name
            current_student['age'] = new_age
            current_student['marks'] = new_marks
            print("\nStudent details updated successfully.")
            return
    
    print("Student Not Found.\n")


def delete_student():

    clear_screen()

    if not students:
        print("Students Not Available.\n")
        return
    
    to_delete = check_if_empty_input("ID")

    for current_student in students:
        if current_student['id'].lower() == to_delete.lower():
            students.remove(current_student)
            print("\nStudent deleted successfully.")
            return
        
    print("Student Not Found.")


def class_statistics():

    clear_screen()

    if not students:
        print("Students Not Available.\n")
        return
    
    highest_marks = students[0]['marks']
    lowest_marks = students[0]['marks']
    total_marks = 0

    for current_student in students:
        if current_student['marks'] < lowest_marks:
           lowest_marks = current_student['marks']
        if current_student['marks'] > highest_marks:
           highest_marks = current_student['marks'] 
        total_marks += current_student['marks']

    average_marks = total_marks / len(students)
    print("Class Statistics\n\n")
    print(f"Highest Marks : {highest_marks}")
    print(f"Lowest Marks : {lowest_marks}")
    print(f"Average Marks : {average_marks}")

def pass_fail_report():

    clear_screen()

    if not students:
        print("Students Not Available.\n")
        return

    print("Pass Students\n\n")
    for current_student in students:
        if current_student['marks'] >= 40:
            print(f"Name : {current_student['name']}")
            print(f"Marks : {current_student['marks']}\n")

    print("Fail Students\n\n")
    for current_student in students:
        if current_student['marks'] < 40:
            print(f"Name : {current_student['name']}")
            print(f"Marks : {current_student['marks']}\n")



# Menu
def show_menu():
    print("===================Student Record Management System (Version 2)================\n")
    print("1. Add Student\n" \
        "2. View Students\n" \
        "3. Search Student\n" \
        "4. Update Student\n" \
        "5. Delete Student\n"
        "6. Class Statistics\n"
        "7. Pass/Fail Report\n"
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
                    add_student()
                case 2:
                    view_students()
                case 3:
                    search_students()
                case 4:
                    update_student()
                case 5:
                    delete_student()
                case 6:
                    class_statistics()
                case 7:
                    pass_fail_report() 
                case 8:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()