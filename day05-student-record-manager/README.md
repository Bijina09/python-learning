# Day 5 - Student Record Manager

## Project

A console-based student record management system that allows users to add, search, update, and delete student records while calculating grades and displaying class statistics.

## Features

- Add students with duplicate name validation
- Validate marks (0–100)
- View all students
- Search students by name
- Update student marks
- Delete students
- Display class statistics
  - Average marks
  - Highest scorer(s)
  - Lowest scorer(s)
  - Total number of students
- Handle invalid menu input using `try`/`except`

## Concepts Practiced

- Functions
- Code reuse
- `try` / `except`
- `return` and `break`
- Lists of dictionaries
- Data validation
- Case-insensitive string comparison
- `enumerate()`
- CRUD operations (Create, Read, Update, Delete)

## What I Learned

- Derived data does not always need to be stored. Instead of storing grades, they can be calculated from marks whenever needed.
- Updating a dictionary through a loop variable updates the original dictionary because both references point to the same object.
- Multiple simple loops can be more readable than combining everything into one complicated loop, while still keeping the overall time complexity as **O(n)**.
- Exception handling prevents the program from crashing due to invalid user input and improves the user experience.

## Future Improvements

- Save student records to a file so data persists after closing the program.
- Add input validation for marks using `try`/`except`.
- Allow updating student names as well as marks.
- Display statistics with formatted decimal places (e.g., `73.33` instead of `73.3333333333`).
