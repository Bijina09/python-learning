import os
import sys

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

# Helper for checking empty input
def check_if_empty_input(prompt):
    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print(f"Input cannot be empty.\n")
        else:
            return entered_value
        
def validate_integer(prompt):
    while True:
        try:
            entered_value = int(check_if_empty_input(prompt))
            return entered_value
        except ValueError:
            print("Input must be an integer.\n")

# Helper for displaying the student details
def display_student_details(current_student,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"\nStudent ID : {current_student['student_id']}\n"
    f"Name : {current_student['name']}\n"
    f"Age : {current_student['age']}\n"
    f"Course : {current_student['course']}\n"
    f"GPA : {current_student['gpa']}\n")

        
class StudentDatabase:   

    def __init__(self):
        self.students = []
        self.load_data()

    def duplicate_student_check(self, prompt, student=None):

        while True:
            duplicate_exists = False

            entered_student_id = validate_integer(prompt)

            for current_student in self.students:
                if current_student['student_id'] == entered_student_id:
                    if current_student is student:
                        continue
                    print("Student already exists.\n")
                    duplicate_exists = True
                    break

            if not duplicate_exists:
                return entered_student_id

    def find_student(self,student_id):

        for current_student in self.students:
            if current_student['student_id'] == student_id:
                return current_student

        return False

    def add_student(self):

        clear_screen()

        entered_student_id = self.duplicate_student_check("Student No")
        entered_name = check_if_empty_input("Name")
        entered_age = validate_integer("Age")
        entered_course = check_if_empty_input("Course")
        entered_gpa = validate_integer("GPA")
        
        student_details = {
            'student_id' : entered_student_id,
            'name' : entered_name,
            'age' : entered_age,
            'course' : entered_course,
            'gpa' : entered_gpa
        }

        self.students.append(student_details)

        print("\nStudent added successfully.\n")
        
    def view_students(self):

        clear_screen()
        
        if not self.students:
            print("No Students Available.\n")
            return
            
        print("Student Details")
        for i, current_student in enumerate(self.students, start=1):
            display_student_details(current_student,i=i)

    def search_student(self):

        clear_screen()
    
        if self.check_if_empty():
            return
        
        to_search = validate_integer("Student ID")
    
        student = self.find_student(to_search)
    
        if not student:
            print("Student Not Found.")
            return
    
        display_student_details(student)

    def update_student(self):

        clear_screen()
    
        if self.check_if_empty():
            return
        
        to_update_student = validate_integer("Roll No")
    
        student = self.find_student(to_update_student)
    
        if not student:
            print("Student Not Found.\n")
            return
    
        student['student_id'] = self.duplicate_student_check("New Student ID",student)
        student['name'] = check_if_empty_input("New Name")
        student['age'] = validate_integer("New Age")
        student['course'] = check_if_empty_input("New Course")
        student['gpa'] = validate_integer("New GPA")
    
        print(f"\nStudent details updated successfully.")

    def delete_student(self):

        clear_screen()
    
        if self.check_if_empty():
            return
    
        to_delete = validate_integer("Student ID")
    
        student = self.find_student(to_delete)
        if not self.student:
            print("Student Not Found.\n")
            return
    
        students.remove(self.students)
        print(f"\nStudent ID {to_delete}, {student['name']} deleted successfully.")
        return

    def save_data(self):

        with open("student_record.txt", "w") as file:
            for each_student in self.students:
                file.write(f"{each_student.values},")

    def load_data(self):
    
        try:
            with open("student_record.txt", "r") as file:
                for line in file:
                    if line.strip(): # Skip empty lines
                        (student_id, 
                        name,
                        age,
                        course,
                        gpa) = line.strip().split(",")

                        student_details = {
                        
                        "student_id" : student_id,
                        "name" : name,
                        "age" : age,
                        "course" : course,
                        "gpa" : gpa 
                    }
                    self.students.append(student_details)
                
        except FileNotFoundError:
            print("Error: The file does not exist.")

    def check_if_empty(self):

        if not self.students:
            print("No Student Records.\n")
            return

students = StudentDatabase()

def show_menu():
    print("===================Student Database================\n")
    print("1. Add Student\n" \
        "2. View All Students\n" \
        "3. Search Student\n" \
        "4. Update Student\n" \
        "5. Delete Student\n" \
        "6. Save Data\n" \
        "7. Load Data\n" \
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
                    students.add_student()
                case 2:
                    students.view_students()
                case 3:
                    students.search_student()
                case 4:
                    students.update_student()
                case 5:
                    students.delete_student()
                case 6:
                    students.save_data()
                case 7:
                    students.load_data()
                case 8:
                    sys.exit(0)
                case _:
                    print("Invalid Choice")

            input("\nPlease press enter to go back to the menu.")

main() 

