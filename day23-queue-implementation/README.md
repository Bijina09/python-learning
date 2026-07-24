# Day 23 - Queue Implementation

## Project

A console-based Queue Implementation program that demonstrates the First In, First Out (FIFO) principle using Python lists through a menu-driven interface.

## Features

- Enqueue element
- Dequeue element
- Peek (Front element)
- Display queue from front to rear
- Check if the queue is empty
- Display queue size
- Peek both front and rear elements
- Clear the queue
- Search for an element in the queue
- Menu-driven interface
- Input validation

## Concepts Practiced

- Functions
- Lists
- Queue (FIFO) operations
- Helper functions
- Input validation
- List methods (`append()`, `pop()`)
- List indexing (`[0]`, `[-1]`)
- `enumerate()`
- Code reusability
- Menu-driven programming

## What I Learned

- A queue follows the **First In, First Out (FIFO)** principle, where the first inserted element is the first one removed.
- Python lists can be used to implement queues using `append()` for insertion and `pop(0)` for deletion.
- Creating helper functions like `queue_empty()` reduces repeated code and improves readability.
- Negative indexing (`[-1]`) provides an easy way to access the rear element of the queue.
- Organizing programs into small, reusable functions makes them easier to understand and maintain.

## Future Improvements

- Implement the queue using `collections.deque` for more efficient dequeue operations.
- Allow searching to display all matching positions if duplicate elements exist.
- Add an option to update an element in the queue.
- Save and load queue data from a file.
- Visualize the queue using ASCII art or a graphical interface.
