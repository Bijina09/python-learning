# Day 18 - Library Management System (Version 3)

## Project

A console-based Library Management System for managing books using a menu-driven interface. The system supports book borrowing, returning, availability tracking, and category-wise analysis.

## Features

- Add new books
- Prevent duplicate Book IDs
- View all books
- Search books by Book ID
- Update book details
- Delete books (only if currently available)
- Borrow books
- Return borrowed books
- View available books
- View borrowed books
- Display the most expensive book(s)
- Count books by category
- Menu-driven interface

## Concepts Practiced

- Functions
- Lists of dictionaries
- Helper functions
- Returning objects from functions
- Input validation
- Boolean status handling
- Nested loops
- Searching data
- Updating dictionaries
- Business logic validation
- Case-insensitive string comparison

## What I Learned

- Business rules can be enforced through program logic, such as preventing deletion of borrowed books.
- Returning `None` from helper functions makes "not found" checks more Pythonic.
- Nested loops can be used to group and count books by category.
- Boolean values can be converted into user-friendly text using helper functions.

## Future Improvements

- Save and load books from a file.
- Search books by title or author.
- Allow multiple copies of the same book.
- Record borrower information.
- Track borrowing and return dates.
- Add late fee calculation.
