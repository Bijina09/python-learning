import sys
import os

# Function for clearing screen
def clear_screen():
    # print("\033[H\033[J", end="")
    os.system("cls" if os.name == "nt" else "clear")

questions = []

# Helper for checking empty input
def check_if_empty_input(prompt):
    while True:
        entered_value = input(f"{prompt} : ").strip()

        if not entered_value:
            print(f"Input cannot be empty.\n")
        else:
            return entered_value

# Helper for displaying the question details
def display_question_details(current_question,i=None):
    if i is not None:
        print(f"\n{i}.")
    print(
    f"Question : {current_question['question']}\n"
    f"A. {current_question['option_A']}\n"
    f"B. {current_question['option_B']}\n"
    f"C. {current_question['option_C']}\n"
    f"D. {current_question['option_D']}\n"
    )
    
# Add Question Function
def add_question():
    
    clear_screen()

    question_details = {}

    while True:
        duplicate_exists = False

        entered_question = check_if_empty_input("Question")

        for current_question in questions:
            if current_question['question'].lower() == entered_question.lower():
                print("Question already exists.\n")
                duplicate_exists = True
                break
        
        if not duplicate_exists:
            break

    entered_optionA = check_if_empty_input("Option A")
    entered_optionB = check_if_empty_input("Option B")
    entered_optionC = check_if_empty_input("Option C")
    entered_optionD = check_if_empty_input("Option D")

    while True:
        entered_correct_answer = check_if_empty_input("Correct Answer")

        if ((entered_correct_answer.lower() == 'a') or 
            (entered_correct_answer.lower() == 'b') or 
            (entered_correct_answer.lower() == 'c') or 
            (entered_correct_answer.lower() == 'd')):
            break
        else:
            print("Answer should be 'A', 'B', 'C' or 'D'\n")
    
    question_details = {
        'question' : entered_question,
        'option_A' : entered_optionA,
        'option_B' : entered_optionB,
        'option_C' : entered_optionC,
        'option_D' : entered_optionD,
        'correct_answer' : entered_correct_answer
    }

    questions.append(question_details)

# View all Questions function
def view_questions():

    clear_screen()

    if not questions:
        print("No Questions Available.\n")
        return
    
    print("Question Details")
    for i, current_question in enumerate(questions, start=1):
        display_question_details(current_question,i=i)

# Deleting question function
def delete_question():

    clear_screen()

    if not questions:
        print("Questions Not Available.\n")
        return

    question_to_delete = check_if_empty_input("Question")

    for current_question in questions:
        if current_question['question'].lower() == question_to_delete.lower():
            questions.remove(current_question)
            print("Question deleted successfully.")
            return
    
    print("Question Not Found.\n")

def display_message(score,questions):
    average = score / len(questions)

    if score < average:
        print("Keep Practicing!")
    elif score == average:
        print("Well Done! You can do more!!")
    else:
        print("Excellent!")

# Function for taking quiz
def start_quiz():

    clear_screen()

    if not questions:
        print("Questions Not Available. Please add questions to take quiz.\n")
        return

    total_score = 0

    for i, current_question in enumerate(questions):
        display_question_details(current_question, i)
        entered_answer = check_if_empty_input("Answer")

        if current_question['correct_answer'].lower() == entered_answer.lower():
            print("Correct!\n\n")
            total_score += 1
        else:
            print("Incorrect")
            print(f"Correct Answer : {current_question['correct_answer']}\n\n")
        
        clear_screen()
        
    print("Quiz Finished!\n")
    print(f"Score : {total_score}/{len(questions)}")
    display_message(total_score,questions)

# Menu
def show_menu():
    print("===================Quiz Management System================\n\n")
    print("1. Add Question\n" \
        "2. View Questions\n" \
        "3. Delete Question\n" \
        "4. Start Quiz\n" \
        "5. Exit\n\n" \
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
                    add_question()
                case 2:
                    view_questions()
                case 3:
                    delete_question()
                case 4:
                    start_quiz()
                case 5:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
            
            input("\n\nPlease press enter to go back to the menu.")
                
main()