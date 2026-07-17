# Day 16 - Employee Record Management System

## Project

A console-based Employee Record Management System for managing employee records, departments, and salary information.

## Features

- Add employees with duplicate Employee ID validation
- View all employees
- Search employees by Employee ID
- Update employee details
- Delete employees
- View employees by department
- Display employee(s) with the highest salary
- View employees with salary greater than Rs. 1 Lakh
- Calculate total salary expense
- Count employees in each department
- Menu-driven interface

## Concepts Practiced

- Functions
- Lists of dictionaries
- CRUD operations (Create, Read, Update, Delete)
- Helper functions for code reuse
- Object identity (`is`) for duplicate validation
- Nested loops
- Custom counters
- Input validation
- Case-insensitive string comparison using `lower()`
- `enumerate()` with `start`

## What I Learned

- A helper function like `find_employee()` reduces repeated searching logic and makes the code easier to maintain.
- Returning the actual dictionary object allows multiple operations (update, delete, display) to work on the same employee without searching again.
- Nested loops can be used to group and count data, such as calculating the number of employees in each department.
- Building small reusable helper functions makes larger programs cleaner and easier to extend.

## Future Improvements

- Save and load employee records from a file.
- Sort employees by salary or name.
- Calculate the average salary by department.
- Search employees by name or department.
- Allow users to enter the minimum salary when viewing high-salary employees instead of using a fixed value.
