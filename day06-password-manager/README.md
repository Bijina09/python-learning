# Day 6 - Password Manager

## Project

A console-based password manager that stores account credentials and allows users to manage them through a menu-driven interface.

## Features

- Add new accounts
- Prevent duplicate website and username combinations
- View all saved accounts
- Hide passwords when viewing all accounts
- Search accounts by website
- Option to reveal passwords after searching
- Delete accounts
- Validate empty input
- Validate minimum password length
- Case-insensitive search and duplicate checking

## Concepts Practiced

- Functions
- Helper functions
- Default function arguments
- Standard library (`getpass`)
- Lists and dictionaries
- Input validation
- Case-insensitive string comparison
- `enumerate()`
- Boolean flags
- `break` and `return`
- `try` / `except`
- `match-case`

## What I Learned

- How to create reusable helper functions to reduce repeated code.
- How default arguments (`hidden=False`) make functions more flexible.
- How to securely accept password input using the `getpass` module.
- How to use a combination of multiple fields (website + username) to identify unique records.

## Future Improvements

- Encrypt or hash stored passwords instead of saving them as plain text.
- Save accounts to a file so data persists after closing the program.
- Edit existing account details.
- Generate strong random passwords.
