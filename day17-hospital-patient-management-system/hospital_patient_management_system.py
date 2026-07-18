import sys
import os

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

patients = []

# Helper for checking empty input
def check_if_empty_input(prompt):
    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print(f"Input cannot be empty.\n")
        else:
            return entered_value

def return_admitted_status(is_admitted):

    return 'Yes' if is_admitted else 'No'
         
# Helper for displaying the patient details
def display_patient_details(current_patient,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"\nPatient ID : {current_patient['patient_id']}\n"
    f"Name : {current_patient['name']}\n"
    f"Age : {current_patient['age']}\n"
    f"Disease : {current_patient['disease']}\n"
    f"Admitted :  {return_admitted_status(current_patient['admitted'])}\n")

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

        if entered_value < 0:
            print(f"Age cannot be negative.\n")
        else:
            return entered_value
        
def duplicate_patient_check(prompt, patient=None):

    while True:
        duplicate_exists = False

        entered_patient_id = validate_integer(prompt)

        for current_patient in patients:
            if current_patient['patient_id'] == entered_patient_id:
                if current_patient is patient:
                    continue
                print("Patient already exists.\n")
                duplicate_exists = True
                break

        if not duplicate_exists:
            return entered_patient_id

def find_patient(patient_id):

    for current_patient in patients:
        if current_patient['patient_id'] == patient_id:
            return current_patient

    return False    

def validate_admitted_status(prompt):

    while True:

        status = check_if_empty_input(prompt)

        if status.lower() == 'n':
            return False
        elif status.lower() == 'y':
            return True 
        
        print("Please enter Y/N.")
                
# Function for adding patient
def add_patient():

    clear_screen()

    entered_patient_id = duplicate_patient_check("Patient ID")
    entered_name = check_if_empty_input("Name")
    entered_age = check_positive("Age")
    entered_disease = check_if_empty_input("Disease")

    patient_details = {
        'patient_id' : entered_patient_id,
        'name' : entered_name,
        'age' : entered_age,
        'disease' : entered_disease,
        'admitted' : True
    }

    patients.append(patient_details)
    print("\nPatient added successfully.\n")

# View all Patients function
def view_all_patients():

    clear_screen()

    if not patients:
        print("No Patients Available.\n")
        return
    
    print("Patient Details")
    for i, current_patient in enumerate(patients, start=1):
        display_patient_details(current_patient,i=i)

# Function for searching patient
def search_patient():

    clear_screen()

    if not patients:
        print("No Patients Available.\n")
        return
    
    to_search = validate_integer("Patient ID")

    patient = find_patient(to_search)

    if not patient:
        print("Patient Not Found.\n")
        return

    display_patient_details(patient)
    

def update_patient_details():

    clear_screen()

    if not patients:
        print("No Patients Available.\n")
        return
    
    to_update_patient = validate_integer("Patient ID")

    patient = find_patient(to_update_patient)

    if not patient:
        print("Patient Not Found.\n")
        return

    patient['patient_id'] = duplicate_patient_check("New Patient ID",patient)
    patient['name'] = check_if_empty_input("New Name")
    patient['age'] = check_positive("New Age")
    patient['disease'] = check_if_empty_input("New Disease")
    patient['admitted'] = validate_admitted_status("New Admitted Status (Y/N)")

    print(f"\nPatient details updated successfully.")

def delete_patient():

    clear_screen()

    if not patients:
        print("No Patients Available.\n")
        return

    to_delete = validate_integer("Patient ID")

    patient = find_patient(to_delete)
    if not patient:
        print("Patient Not Found.\n")
        return

    patients.remove(patient)
    print(f"\nPatient ID {to_delete}, {patient['name']} deleted successfully.")
    return

def view_admitted_patients():

    clear_screen()

    if not patients:
        print("No Patients Available.\n")
        return

    print("Admitted Patients:\n")
    i = 0
    for current_patient in patients:
        if current_patient['admitted']:           
            i += 1
            display_patient_details(current_patient, i)

    if i == 0:
        print(f"No Patients Currently Admitted.")

def view_discharged_patients():

    clear_screen()

    if not patients:
        print("No Patients Available.\n")
        return

    print("Discharged Patients:\n")
    i = 0
    for current_patient in patients:
        if not current_patient['admitted']:
            i += 1
            display_patient_details(current_patient, i)
    
    if i == 0:
        print(f"No Patients Currently Discharged.")

def count_total_admitted_patients():
    
    clear_screen()

    if not patients:
        print("No Patients Available.\n")
        return

    total_count = 0

    for current_patient in patients:
        if current_patient['admitted']:
            total_count += 1

    print(f"Total Admitted Patients: {total_count}")

def find_oldest_patient():

    clear_screen()

    if not patients:
        print("No Patients Available.\n")
        return
    
    oldest_age = patients[0]['age']

    for current_patient in patients:
        if current_patient['age'] > oldest_age:
            oldest_age = current_patient['age']

    print("Oldest Patient(s): \n")
    i = 0
    for current_patient in patients:
        if current_patient['age'] == oldest_age:
            i += 1
            display_patient_details(current_patient, i)

    
def show_menu():
    print("===================Hospital Patient Management System================\n")
    print("1. Add Patient\n" \
        "2. View All Patients\n" \
        "3. Search Patient\n" \
        "4. Update Patient Details\n" \
        "5. Delete Patient\n"
        "6. View Admitted Patients\n"
        "7. View Discharged Patients\n"
        "8. Count Total Admitted Patients\n"
        "9. Find Oldest Patient\n"
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
                    add_patient()
                case 2:
                    view_all_patients()
                case 3:
                    search_patient()
                case 4:
                    update_patient_details()
                case 5:
                    delete_patient()
                case 6:
                    view_admitted_patients()
                case 7:
                    view_discharged_patients()
                case 8:
                    count_total_admitted_patients()
                case 9:
                    find_oldest_patient() 
                case 10:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()