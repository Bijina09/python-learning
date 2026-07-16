# Day 15 - Student Record Management System (Version 3)

## Project

A console-based Student Record Management System for managing student records and analyzing academic performance.

## Features

- Add new students
- Prevent duplicate roll numbers
- View all students
- Search students by roll number
- Update student details
- Delete students
- View passed students
- View failed students
- Display top scorer(s)
- Calculate class average
- Menu-driven interface

## Concepts Practiced

- Functions
- Lists of dictionaries
- Helper functions for code reuse
- Input validation
- Boolean values
- Object identity (`is`)
- Default function parameters (`None`)
- Returning objects from helper functions
- `enumerate()` with `start`
- Formatted floating-point output (`:.2f`)

## What I Learned

- Returning an object from a helper function makes code shorter and avoids searching through the list multiple times.
- `is` compares object identity, which is useful when updating a record without treating it as a duplicate.
- Boolean helper functions can simplify conditions and improve readability.
- Input validation functions make programs more reliable and reduce repeated code.
- Formatting numbers with `:.2f` displays floating-point values with two decimal places.

## Future Improvements

- Save and load student records from a file.
- Search students by name in addition to roll number.
- Sort students by roll number or marks.
- Display the lowest scorer(s).
- Add more class statistics such as median and pass percentage.
