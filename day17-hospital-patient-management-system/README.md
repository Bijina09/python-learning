# Day 17 - Hospital Patient Management System

## Project

A console-based Hospital Patient Management System for managing patient records and tracking their admission status.

## Features

- Add new patients
- Prevent duplicate Patient IDs
- View all patients
- Search patients by Patient ID
- Update patient details
- Delete patients
- View admitted patients
- View discharged patients
- Count total admitted patients
- Find oldest patient(s)
- Menu-driven interface

## Concepts Practiced

- Functions
- Lists of dictionaries
- Boolean values (`True` / `False`)
- Helper functions for code reuse
- Data validation
- Integer validation using `try` / `except`
- Duplicate checking
- Case-insensitive string comparison using `lower()`
- Conditional expressions (ternary operator)
- `enumerate()` with `start`
- CRUD operations (Create, Read, Update, Delete)

## What I Learned

- Boolean values can represent real-world states, such as whether a patient is admitted or discharged.
- A helper function can convert internal boolean values into user-friendly output like "Yes" and "No".
- Business rules can simplify a program—for example, assuming every new patient is admitted by default and allowing the admission status to change only during updates.
- Reusing helper functions for searching, validation, and displaying data makes the code easier to maintain and avoids duplication.
- Returning objects from helper functions allows multiple operations to work with the same data without repeating search logic.

## Future Improvements

- Store the admission and discharge dates.
- Add doctor and room assignment for each patient.
- Save and load patient records from a file.
- Search patients by name or disease.
- Display statistics such as the average patient age.
