import sys
import os

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

employees = []

# Helper for checking empty input
def check_if_empty_input(prompt):
    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print(f"Input cannot be empty.\n")
        else:
            return entered_value
        
# Helper for displaying the employee details
def display_employee_details(current_employee,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"\nEmployee ID : {current_employee['employee_id']}\n"
    f"Name : {current_employee['name']}\n"
    f"Department : {current_employee['department']}\n"
    f"Salary : Rs. {current_employee['salary']}\n")

# Helper for displaying the department details
def display_department_details(current_department,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"\nDepartment Name : {current_department['name']}\n"
    f"Count : {current_department['count']}\n")

def validate_integer(prompt):
    while True:
        try:
            entered_value = int(check_if_empty_input(prompt))
            return entered_value
        except ValueError:
            print("Input must be an integer.\n")

# Helper for checking empty input
def check_positive(prompt):
    while True:
        entered_value = validate_integer(prompt)

        if entered_value <= 0:
            print(f"Salary cannot be negative/Zero.\n")
        else:
            return entered_value
        
def duplicate_employee_check(prompt, employee=None):

    while True:
        duplicate_exists = False

        entered_employee_id = validate_integer(prompt)

        for current_employee in employees:
            if current_employee['employee_id'] == entered_employee_id:
                if current_employee is employee:
                    continue
                print("Employee already exists.\n")
                duplicate_exists = True
                break

        if not duplicate_exists:
            return entered_employee_id

def find_employee(employee_id):

    for current_employee in employees:
        if current_employee['employee_id'] == employee_id:
            return current_employee

    return False    

# Function for adding employee
def add_employee():

    clear_screen()

    entered_employee_id = duplicate_employee_check("Employee ID")
    entered_name = check_if_empty_input("Name")
    entered_department = check_if_empty_input("Department")
    entered_salary = check_positive("Salary")

    employee_details = {
        'employee_id' : entered_employee_id,
        'name' : entered_name,
        'department' : entered_department,
        'salary' : entered_salary
    }

    employees.append(employee_details)
    print("\nEmployee added successfully.\n")

# View all Employees function
def view_all_employees():

    clear_screen()

    if not employees:
        print("No Employees Available.\n")
        return
    
    print("Employee Details")
    for i, current_employee in enumerate(employees, start=1):
        display_employee_details(current_employee,i=i)

# Function for searching employee
def search_employee():

    clear_screen()

    if not employees:
        print("No Employees Available.\n")
        return
    
    to_search = validate_integer("Employee ID")

    employee = find_employee(to_search)

    if not employee:
        print("Employee Not Found.")
        return

    display_employee_details(employee)
    

def update_employee_details():

    clear_screen()

    if not employees:
        print("No Employees Available.\n")
        return
    
    to_update_employee = validate_integer("Employee ID")

    employee = find_employee(to_update_employee)

    if not employee:
        print("Employee Not Found.\n")
        return

    employee['employee_id'] = duplicate_employee_check("New Employee ID",employee)
    employee['name'] = check_if_empty_input("New Name")
    employee['department'] = check_if_empty_input("New Department")
    employee['salary'] = check_positive("New Salary")

    print(f"\nEmployee details updated successfully.")

def delete_employee():

    clear_screen()

    if not employees:
        print("No Employees Available.\n")
        return

    to_delete = validate_integer("Employee ID")

    employee = find_employee(to_delete)
    if not employee:
        print("Employee Not Found.\n")
        return

    employees.remove(employee)
    print(f"\nEmployee ID {to_delete}, {employee['name']} deleted successfully.")
    return

def view_employees_by_department():

    clear_screen()

    if not employees:
        print("No Employees Available.\n")
        return

    department_to_view = check_if_empty_input("Department")

    i = 0
    for current_employee in employees:
        if current_employee['department'].lower() == department_to_view.lower():            
            i += 1
            display_employee_details(current_employee, i)

    if i == 0:
        print(f"No Employees Present in Department '{department_to_view}'.")

def display_highest_salary():

    clear_screen()

    if not employees:
        print("No Employees Available.\n")
        return

    highest_salary = employees[0]['salary']

    for current_employee in employees:
        if current_employee['salary'] > highest_salary:
            highest_salary = current_employee['salary']

    print(f"Highest Salary : Rs. {highest_salary}\n")
    print("Employee(s) with Highest Salary:\n")
    i = 0
    for current_employee in employees:
        if current_employee['salary'] == highest_salary:
            i += 1
            display_employee_details(current_employee, i)

def view_high_salary_employees():
    
    clear_screen()

    if not employees:
        print("No Employees Available.\n")
        return

    high_salary_baseline = 100000

    print("Employee(s) with Salary Greater than 1 Lakh:\n")
    i = 0
    for current_employee in employees:
        if current_employee['salary'] > high_salary_baseline:
            i += 1
            display_employee_details(current_employee, i)

    if i == 0:
        print("No Employees Found.")

def count_employees_per_department():
    clear_screen()

    if not employees:
        print("No Employees Available.\n")
        return
    
    departments = []

    for current_employee in employees:
        duplicate = False

        for current_department in departments:
            if current_department['name'] == current_employee['department']:
                duplicate = True
                break

        if not duplicate:
            departments.append({
                'name': current_employee['department']
        })

    for each_employee in employees:
        for current_department in departments:
            if each_employee['department'] == current_department['name']:
                if 'count' not in current_department:
                    current_department['count'] = 0
                current_department['count'] += 1
                break

    for i, current_department in enumerate(departments, start=1):
        display_department_details(current_department, i)


def calculate_total_salary_expense():

    clear_screen()

    if not employees:
        print("No Employees Available.\n")
        return

    total_salary_expense = 0

    for current_employee in employees:
        total_salary_expense += current_employee['salary']

    print(f"Total Salary Expense: Rs. {total_salary_expense}")
    
def show_menu():
    print("===================Employee Record Management System================\n")
    print("1. Add Employee\n" \
        "2. View All Employees\n" \
        "3. Search Employee\n" \
        "4. Update Employee Details\n" \
        "5. Delete Employee\n"
        "6. View Employees by Department\n"
        "7. Display Highest Salary\n"
        "8. View High Salary Employees\n"
        "9. Calculate Total Salary Expense\n"
        "10. Show no. of Employees per Department\n"
        "11. Exit\n\n" \
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
                    add_employee()
                case 2:
                    view_all_employees()
                case 3:
                    search_employee()
                case 4:
                    update_employee_details()
                case 5:
                    delete_employee()
                case 6:
                    view_employees_by_department()
                case 7:
                    display_highest_salary()
                case 8:
                    view_high_salary_employees()
                case 9:
                    calculate_total_salary_expense() 
                case 10:
                    count_employees_per_department()
                case 11:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()