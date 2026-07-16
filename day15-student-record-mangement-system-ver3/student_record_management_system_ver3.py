import sys
import os

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

students = []

# Helper for checking empty input
def check_if_empty_input(prompt):
    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print(f"Input cannot be empty.\n")
        else:
            return entered_value
        
# Helper for displaying the student details
def display_student_details(current_student,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"\nRoll No : {current_student['roll_no']}\n"
    f"Name : {current_student['name']}\n"
    f"Marks : {current_student['marks']}\n")

def validate_integer(prompt):
    while True:
        try:
            entered_value = int(check_if_empty_input(prompt))
            return entered_value
        except ValueError:
            print("Input must be an integer.\n")

def duplicate_student_check(prompt, student=None):

    while True:
        duplicate_exists = False

        entered_roll_no = validate_integer(prompt)

        for current_student in students:
            if current_student['roll_no'] == entered_roll_no:
                if current_student is student:
                    continue
                print("Student already exists.\n")
                duplicate_exists = True
                break

        if not duplicate_exists:
            return entered_roll_no

def find_student(roll_no):

    for current_student in students:
        if current_student['roll_no'] == roll_no:
            return current_student

    return False    

def is_pass(marks):
    # Shorter, simpler way
    return marks >= 40

    
# Function for validating and getting marks
def validate_marks(prompt):

    while True:

        entered_marks = validate_integer(prompt)
        if 0 <= entered_marks <= 100:
            return entered_marks 
        else:
            print("Marks should be between 0 and 100.\n")

# Function for adding student
def add_student():

    clear_screen()

    entered_roll_no = duplicate_student_check("Roll No")
    entered_name = check_if_empty_input("Name")
    entered_marks = validate_marks("Marks")

    student_details = {
        'roll_no' : entered_roll_no,
        'name' : entered_name,
        'marks' : entered_marks
    }

    students.append(student_details)
    print("\nStudent added successfully.\n")

# View all Students function
def view_all_students():

    clear_screen()

    if not students:
        print("No Students Available.\n")
        return
    
    print("Student Details")
    for i, current_student in enumerate(students, start=1):
        display_student_details(current_student,i=i)

# Function for searching student
def search_student():

    clear_screen()

    if not students:
        print("Students Not Available.\n")
        return
    
    to_search = validate_integer("Roll No")

    student = find_student(to_search)

    if not student:
        print("Student Not Found.")
        return

    display_student_details(student)
    

def update_student():

    clear_screen()

    if not students:
        print("No Students Available.\n")
        return
    
    to_update_student = validate_integer("Roll No")

    student = find_student(to_update_student)

    if not student:
        print("Student Not Found.\n")
        return

    student['roll_no'] = duplicate_student_check("New Roll No",student)
    student['name'] = check_if_empty_input("New Name")
    student['marks'] = validate_marks("New Marks")

    print(f"\nStudent details updated successfully.")

def delete_student():

    clear_screen()

    if not students:
        print("No Students Available.\n")
        return

    to_delete = validate_integer("Roll No")

    student = find_student(to_delete)
    if not student:
        print("Student Not Found.\n")
        return

    students.remove(student)
    print(f"\nRoll No {to_delete}, {student['name']} deleted successfully.")
    return

def view_passed_students():

    clear_screen()

    if not students:
        print("No Students Available.\n")
        return

    i = 0
    for current_student in students:
        if is_pass(current_student['marks']):
            i += 1
            display_student_details(current_student, i)

    if i == 0:
        print("No Students Passed.")

def view_failed_students():

    clear_screen()

    if not students:
        print("No Students Available.\n")
        return

    i = 0
    for current_student in students:
        if not is_pass(current_student['marks']):
            i += 1
            display_student_details(current_student, i)

    if i == 0:
        print("No Students Failed.")

def display_top_scorer():

    clear_screen()

    if not students:
        print("No Students Available.\n")
        return

    highest_score = students[0]['marks']

    for current_student in students:
        if current_student['marks'] > highest_score:
            highest_score = current_student['marks']

    print(f"Highest Score : {highest_score}\n")
    print("Top Scorer(s):\n")
    i = 0
    for current_student in students:
        if current_student['marks'] == highest_score:
            i += 1
            display_student_details(current_student, i)

def calculate_class_average():

    clear_screen()

    if not students:
        print("No Students Available.\n")
        return

    total_score = 0

    for current_student in students:
        total_score += current_student['marks']

    print(f"Class Average : {total_score/len(students):.2f}")
    
def show_menu():
    print("===================Student Record Management System (Version 3)================\n\n")
    print("1. Add Student\n" \
        "2. View All Students\n" \
        "3. Search Student\n" \
        "4. Update Student\n" \
        "5. Delete Student\n"
        "6. View Passed Students\n"
        "7. View Failed Students\n"
        "8. Display Top Scorer\n"
        "9. Calculate Class Average\n"
        "10. Exit\n\n" \
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
                    view_all_students()
                case 3:
                    search_student()
                case 4:
                    update_student()
                case 5:
                    delete_student()
                case 6:
                    view_passed_students()
                case 7:
                    view_failed_students()
                case 8:
                    display_top_scorer()
                case 9:
                    calculate_class_average() 
                case 10:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()