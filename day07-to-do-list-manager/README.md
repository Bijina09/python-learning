# Day 7 - To-Do List

## Project

A console-based To-Do List application for managing daily tasks.

## Features

- Add new tasks
- Prevent duplicate task titles
- View all tasks
- Mark tasks as completed or pending
- View only completed tasks
- View only pending tasks
- Delete tasks
- Menu-driven interface

## Concepts Practiced

- Functions
- Boolean values (`True` / `False`)
- Conditional statements
- Lists of dictionaries
- Input validation
- Case-insensitive string comparison using `lower()`
- Helper functions to reduce code duplication
- Manual counters for filtered output

## What I Learned

- A helper function should have a single responsibility.
- Returning a simple confirmation (`True`/`False`) can lead to cleaner program flow than making a helper handle multiple responsibilities.
- Not every repeated line of code should be abstracted away—it's more important to reduce duplicated responsibilities than duplicated syntax.
- Sometimes a simple solution is more readable than a more "clever" abstraction.

## Future Improvements

- Add due dates and priorities.
- Sort tasks by status or due date.
- Save tasks to a file so they persist after closing the program.
- Edit task titles.
- Display task completion statistics.
