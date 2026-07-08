import sys

def clear_screen():
    print("\033[H\033[J", end="")

tasks = []

def check_if_empty_input(prompt):
    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
                print("Input cannot be empty.\n\n")
        else:
            return entered_value

def add_task():

    clear_screen()

    task_details = {}
    while True:
        duplicate_exists = False
        entered_title = check_if_empty_input("Enter the task title")

        for current_task in tasks:
            if current_task['title'].lower() == entered_title.lower():
                print("Task already exists.")
                duplicate_exists = True
                break
        
        if not duplicate_exists:
            break

    task_details['title'] = entered_title
    task_details['completed'] = False 

    tasks.append(task_details)

def view_all_tasks():

    clear_screen()

    if not tasks:
        print("No Tasks Available.\n")
        return
    
    for i, current_task in enumerate(tasks):
        print(f"{i+1}.\n"
              f"Title : {current_task['title']}")
        if current_task['completed']:
            print(f"Status : Completed\n\n")
        else:
            print(f"Status : Pending\n\n")

def confirm_changing_status():
    while True:
        response_to_change = check_if_empty_input("Do you want to change the status? (y/n)")
        if response_to_change.lower() == 'y':
            return True
        elif response_to_change.lower() == 'n':
            return False
        else:
            print("Please enter y/n.")

def update_task_status():

    clear_screen()
    
    if not tasks:
        print("No Tasks Available.\n")
        return
    
    to_change_status = check_if_empty_input("Title")

    for current_task in tasks:
        if current_task['title'].lower() == to_change_status.lower():
            if not current_task['completed']:
                print("\nStatus : Pending") 

                if confirm_changing_status():  
                    current_task['completed'] = True
                    print("Successfully marked as completed.\n") 
                return
            else:
                print("Status : Completed\n")
                if confirm_changing_status():
                    current_task['completed'] = False
                    print("Successfully marked as pending.\n")
                return

    print("Task Not Found.\n")

def view_completed_tasks():

    clear_screen()

    if not tasks:
        print("No Tasks Available.\n")
        return
    
    task_completed = False

    i = 0
    for current_task in tasks:
        if current_task['completed']:
            task_completed = True
            i+=1
            print(f"{i}.\n"
                  f"Title : {current_task['title']}\n\n")

    if not task_completed:
        print("No Completed Task.\n")

def view_pending_tasks():

    clear_screen()

    if not tasks:
        print("No Tasks Available.\n")
        return
    
    task_pending = False
    i = 0
    for current_task in tasks:
        if not current_task['completed']:
            task_pending = True
            i+=1
            print(f"{i}.\n"
                  f"Title : {current_task['title']}\n\n")

    if not task_pending:
        print("No Pending Task.\n")

def delete_task():

    clear_screen()

    if not tasks:
        print("No Tasks Available.\n")
        return
    
    task_to_delete = check_if_empty_input("Title")

    for current_task in tasks:
        if current_task['title'].lower() == task_to_delete.lower():
            tasks.remove(current_task)
            print("Task Deleted Successfully.\n")
            return 
        
    print("No Task Found.\n")


def show_menu():
    print("===================To-Do List================\n\n")
    print("1. Add Task\n" \
        "2. View All Tasks\n" \
        "3. Update Task Status\n" \
        "4. View Completed Tasks\n" \
        "5. View Pending Tasks\n"
        "6. Delete Task\n"
        "7. Exit\n\n" \
        "Enter your choice: ")
    
def main():

    while True:

        clear_screen ()

        show_menu()

        try:
            choice = int(input())
        except ValueError:
            print("\nError: Please enter a valid integer\n")
            input("\nPress enter to continue")
        else:
            match choice:
                case 1:
                    add_task()
                case 2:
                    view_all_tasks()
                case 3:
                    update_task_status()
                case 4:
                    view_completed_tasks()
                case 5:
                    view_pending_tasks()
                case 6:
                    delete_task()
                case 7:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()