# Day 12 - Personal Expense Tracker (Version 2)

## Project

A console-based Personal Expense Tracker for recording daily expenses, searching expenses by category, generating reports, and tracking spending.

## Features

- Add new expenses
- View all expenses
- Search expenses by category
- Delete expenses by expense number
- Calculate total spending
- Generate daily expense report
- View highest expense
- Validate dates (real dates only)
- Prevent future dates
- Validate integer inputs
- Menu-driven interface

## Concepts Practiced

- Functions
- Lists of dictionaries
- Helper functions for code reuse
- Input validation
- Exception handling (`try` / `except`)
- Keyword `raise`
- Date validation using `datetime`
- Working with `date.today()`
- `enumerate()` with `start`
- Conditional statements
- Loops
- Aggregation using accumulators
- Finding maximum values in a list

## What I Learned

- `datetime.strptime()` can validate whether a date actually exists instead of only checking its format.
- Helper functions make validation reusable and reduce duplicated code.
- Separating responsibilities makes functions easier to read and maintain.
- User input should always be validated before processing.
- Small improvements in validation can greatly improve the reliability of a program.

## Future Improvements

- Save and load expenses from a file.
- Update existing expenses.
- Search expenses by date.
- Generate monthly expense reports.
- Support decimal amounts instead of only integers.
- Add expense categories from a predefined list.
- Display spending summaries by category.
