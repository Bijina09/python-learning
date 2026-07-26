# Day 25 - Doubly Linked List Implementation

## Project

A console-based Doubly Linked List implementation built using Object-Oriented Programming (OOP) in Python. The program uses a menu-driven interface to perform common doubly linked list operations by creating and managing nodes manually with both `next` and `prev` references.

## Features

- Add node at the end
- Add node at the beginning
- Display linked list in forward direction
- Display linked list in backward direction
- Search for a node
- Delete a node
- Count total nodes
- Check if the linked list is empty
- Clear the linked list
- Menu-driven interface

## Concepts Practiced

- Classes and Objects
- Object-Oriented Programming (OOP)
- Doubly Linked List data structure
- Nodes and references
- Forward traversal
- Backward traversal
- Pointer manipulation using `next` and `prev`
- Helper functions
- Loops
- Conditional statements
- Menu-driven programming
- Edge case handling

## What I Learned

- A doubly linked list stores data as a chain of nodes, where each node points to both the next node and the previous node.
- Maintaining both `next` and `prev` references allows traversal in both forward and backward directions.
- Insertion at the beginning requires updating the old head node’s `prev` pointer and moving the head to the new node.
- Insertion at the end requires connecting the new node with the last node in both directions.
- Deleting a node requires reconnecting neighboring nodes by updating both `next` and `prev` pointers correctly.
- The head node is a special case during deletion because it does not have a previous node and the head reference must be updated separately.
- Handling edge cases such as deleting the first node, last node, middle node, and nodes from a single-node list is important for a correct implementation.
- Separating helper methods from display methods improves code reusability and readability.

## Future Improvements

- Insert a node at a specific position.
- Delete a node by position.
- Update a node’s value.
- Maintain a `tail` pointer for more efficient insertion at the end.
- Reverse the doubly linked list.
- Sort the linked list.
- Remove duplicate nodes.
- Implement Circular Doubly Linked List.
