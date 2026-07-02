print("Enter the number of students:")
no_of_students = int(input())

student = []
for _ in range(no_of_students):

    student_data = {}
    student_data['name'] = input("Enter the name of the student: ")
    while True:
        student_data['marks'] = int(input("Enter the marks of the student(0-100): "))

        if 0 <= student_data['marks'] <= 100:
            break
    
    student.append(student_data)


total_marks = 0
for student_data in student:
    
    total_marks += student_data['marks']

average_marks = total_marks/no_of_students

## For Highest Scorer
highest_marks = student[0]['marks']
highest_scorer = student[0]['name']

## For Lowest Scorer
lowest_marks = student[0]['marks']
lowest_scorer = student[0]['name']

for student_data in student:

    ### Highest Logic
    if(student_data['marks'] > highest_marks ):
        highest_marks = student_data['marks']
        highest_scorer = student_data['name']

    ### Lowest Logic
    if(student_data['marks'] < lowest_marks ):
        lowest_marks = student_data['marks']
        lowest_scorer = student_data['name']
    
    ###Grade Logic
    if 90 <= student_data['marks'] <= 100:
        student_data['grade'] = 'A'
    elif 80 <= student_data['marks'] <= 89:
        student_data['grade'] = 'B'
    elif 70 <= student_data['marks'] <= 79:
        student_data['grade'] = 'C'
    elif 60 <= student_data['marks'] <= 69:
        student_data['grade'] = 'D'
    else:
        student_data['grade'] = 'F'

# Student Report

print("------------------Student Report----------------------\n\n")

for student_data in student:
    print(f"Name : {student_data['name']}\n")
    print(f"Marks : {student_data['marks']}\n")
    print(f"Grade : {student_data['grade']}\n\n")

print(f"Average Marks : {average_marks}\n\n")
print(f"Highest Scorer : {highest_scorer} ({highest_marks})\n\n")
print(f"Lowest Scorer : {lowest_scorer} ({lowest_marks})")
