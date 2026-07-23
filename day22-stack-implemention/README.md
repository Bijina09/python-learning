# Day 22 - Stack Implementation

## Project

A console-based Stack Implementation that demonstrates the Last-In, First-Out (LIFO) principle through a menu-driven interface.

## Features

- Push an element onto the stack
- Pop the top element
- Peek at the top element without removing it
- Display the stack from top to bottom
- Check whether the stack is empty
- Input validation
- Menu-driven interface

## Concepts Practiced

- Lists as a stack
- Stack operations (Push, Pop, Peek)
- LIFO (Last-In, First-Out)
- Functions
- Helper functions
- Input validation
- List methods (`append()`, `pop()`)
- Negative indexing (`[-1]`)
- List slicing (`[::-1]`)
- Code reuse (DRY Principle)

## What I Learned

- A stack follows the Last-In, First-Out (LIFO) principle, where the most recently added element is the first one removed.
- Python lists can efficiently implement a stack using `append()` and `pop()`.
- The top element can be accessed directly using negative indexing (`stack[-1]`) without traversing the entire list.
- Creating reusable helper functions such as `stack_empty()` reduces duplicated code and improves readability.
- Displaying the stack in reverse order provides a more intuitive visualization of the stack structure.

## Future Improvements

- Implement a stack with a maximum capacity.
- Allow searching for an element in the stack.
- Display the current stack size.
- Keep a history of push and pop operations.
- Implement the stack using a linked list instead of a Python list.
