# Day 29 - File-Based Student Database System

## Project

A console-based Student Database System built using Object-Oriented Programming (OOP) and Python file handling. The program uses a menu-driven interface to perform CRUD (Create, Read, Update, Delete) operations while storing student records permanently in a text file.

## Features

- Add student
- View all students
- Search for a student
- Update student details
- Delete a student
- Save student records to a file
- Load student records from a file
- Prevent duplicate Student IDs
- Check if the database is empty
- Menu-driven interface

## Concepts Practiced

- Classes and Objects
- Object-Oriented Programming (OOP)
- File Handling
- Reading and Writing Files
- CRUD Operations
- Lists and Dictionaries
- Helper Functions
- Input Validation
- Searching
- Menu-driven Programming
- Edge Case Handling

## What I Learned

- File handling allows data to persist even after the program is closed.
- Student records can be converted into a text format for storage and reconstructed when loading the program.
- Separating helper functions from database operations improves code organization and readability.
- Encapsulating database operations inside a class makes the program easier to maintain.
- Input validation helps prevent invalid or duplicate data from being stored.
- Reading data from a file and writing updated records back ensures the database remains synchronized.
- Designing CRUD operations becomes more practical when combined with persistent storage.

## Future Improvements

- Store data in JSON format instead of plain text.
- Use the `csv` module for better file handling.
- Store records in an SQLite database.
- Sort students by ID, name, or GPA.
- Calculate the average GPA of all students.
- Search students by course.
- Export records to a CSV file.
- Add user authentication for database access.
