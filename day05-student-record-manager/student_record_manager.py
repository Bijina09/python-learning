import sys

def clear_screen():
    print("\033[H\033[J", end="")

students = []

def assign_grade(marks):

    #Grade Logic
    if 90 <= marks <= 100:
        return 'A'
    elif 80 <= marks <= 89:
        return 'B'
    elif 70 <= marks <= 79:
        return 'C'
    elif 60 <= marks <= 69:
        return 'D'
    else:
        return 'F'

def validate_marks(marks):

    while True:
        if  0 <= marks <= 100:
            return marks
        else:
            print("Marks should be between 0 and 100\n")
            marks = int(input("Enter the marks: "))

def add_student():
    clear_screen()

    student_details = {}

    while True:
        duplicate_exists = False

        entered_name = input("Enter the name: ")

        for current_student in students:
            if current_student['name'].lower() == entered_name.lower():
                print("Student already exits.\n")
                duplicate_exists = True
                break

        if not duplicate_exists:
            break

    entered_marks = int(input("Enter the marks: "))

    student_details['name'] = entered_name
    student_details['marks'] = validate_marks(entered_marks)

    students.append(student_details)

def view_students():

    clear_screen()

    if not students:
        print("\nNo students Found.")
        return 
    
    for i, current_student in enumerate(students):
        grade = assign_grade(current_student['marks'])
        print(f"{i+1}.\n"
              f"Name : {current_student['name']}\n"
              f"Marks : {current_student['marks']}\n"
              f"Grade : {grade}\n\n"
              )

def search_student():

    clear_screen()

    if not students:
        print("\nNo students Found.")
        return 

    to_search = input("Enter the name of the student: ")

    for current_student in students:
        if current_student['name'].lower() == to_search.lower():
            grade = assign_grade(current_student['marks'])
            print(f"Name : {current_student['name']}\n"
                  f"Marks : {current_student['marks']}\n"
                  f"Grade : {grade}\n")
            return
    
    print("\nNo Student Found.")

def update_marks():

    clear_screen()

    if not students:
        print("\nNo students Found.")
        return 

    to_update_student = input("Enter student name: ")  

    for current_student in students:
        if current_student['name'].lower() == to_update_student.lower():

            new_marks = int(input("New Marks: "))
            
            current_student['marks'] = validate_marks(new_marks)

            print("\nMarks updated successfully.")
            return
    
    print("\nNo Student Found.")
        
def delete_student():

    clear_screen()

    if not students:
        print("\nNo students Found.")
        return 

    to_delete = input("Enter student name: ")

    for current_student in students:
        if current_student['name'].lower() == to_delete.lower():
            students.remove(current_student)
            print("\nStudent deleted successfully.")
            return
    
    print("\nNo Student Found.")

def show_class_statistics():

    clear_screen()

    if not students:
        print("\nNo students Found.")
        return 

    total_marks = 0
    highest_score = students[0]['marks']
    lowest_score = students[0]['marks']
    total_students = len(students)

    for current_student in students:
        total_marks += current_student['marks']

    average_marks = total_marks/total_students

    print(f"Average Marks : {average_marks}\n\n")

    for current_student in students:
        if current_student['marks'] > highest_score:
            highest_score = current_student['marks']
        if current_student['marks'] < lowest_score:
            lowest_score = current_student['marks']

    print("Highest Scorer:\n")
    for current_student in students:    
        if current_student['marks'] == highest_score:
            print(f"{current_student['name']}\n")

    print("\nLowest Scorer:\n")
    for current_student in students:
        
        if current_student['marks'] == lowest_score:
            print(f"{current_student['name']}\n")

    print(f"\nNumber of students : {total_students}")


def show_menu():

    print("===================Student Record Manager==================\n\n" \
    "1. Add Student\n" \
    "2. View Students\n" \
    "3. Search Student\n" \
    "4. Update Marks\n" \
    "5. Delete Student\n" \
    "6. Show Class Statistics\n" \
    "7. Exit\n\n" \
    "Enter your choice: ")

def main():

    while True:

        clear_screen()

        show_menu()

        try:
            choice = int(input())
            
        except ValueError:
            print("\nError: Please enter a valid integer.")
            input("\n\nPress enter to continue.")
        else :
            match choice:

                case 1:
                    add_student()
                case 2:
                    view_students()
                case 3:
                    search_student()
                case 4:
                    update_marks()
                case 5:
                    delete_student()
                case 6:
                    show_class_statistics()
                case 7:
                    sys.exit(0)
                case _:
                    print("Invalid Choice.")
        
            input("\n\nPlease press enter to go back to the menu.")
            

main()




