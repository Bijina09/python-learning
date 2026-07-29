# Day 26-28 - Binary Search Tree Implementation

## Project

A console-based Binary Search Tree (BST) implementation built using Object-Oriented Programming (OOP) in Python. The program uses a menu-driven interface to perform common Binary Search Tree operations using recursive algorithms for insertion, searching, traversal, and node counting.

## Features

- Insert node
- Search for a node
- Inorder traversal
- Preorder traversal
- Postorder traversal
- Find minimum value
- Find maximum value
- Count total nodes
- Check if the tree is empty
- Menu-driven interface

## Concepts Practiced

- Classes and Objects
- Object-Oriented Programming (OOP)
- Binary Search Tree (BST)
- Tree nodes and references
- Recursion
- Tree traversal algorithms
- Recursive searching
- Recursive insertion
- Helper functions
- Conditional statements
- Menu-driven programming
- Edge case handling

## What I Learned

- A Binary Search Tree stores data in a hierarchical structure where values smaller than a node are placed in the left subtree and larger values in the right subtree.
- Recursive functions naturally fit tree-based data structures because each subtree is itself another Binary Search Tree.
- Inorder traversal visits nodes in the order Left → Root → Right and produces values in ascending order for a Binary Search Tree.
- Preorder traversal visits nodes in the order Root → Left → Right, while Postorder traversal follows Left → Right → Root.
- Searching becomes more efficient by comparing the target value and recursively moving only to the required subtree instead of checking every node.
- Finding the minimum value requires repeatedly moving to the leftmost node, while finding the maximum value requires moving to the rightmost node.
- Recursive functions can return values from subtrees, allowing operations such as counting total nodes without using global or class variables.
- Handling edge cases such as an empty tree and duplicate values is important for maintaining a valid Binary Search Tree.

## Future Improvements

- Delete a node from the Binary Search Tree.
- Calculate the height of the tree.
- Check whether the tree is balanced.
- Perform Level Order Traversal (Breadth-First Search).
- Display leaf nodes and internal nodes separately.
- Mirror the Binary Search Tree.
- Balance the tree automatically after insertion.
- Visualize the Binary Search Tree structure in the console.
