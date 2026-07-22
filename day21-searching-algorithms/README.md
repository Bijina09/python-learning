# Day 21 - Searching Algorithms

## Project

A console-based Searching Algorithms program that allows users to enter a list of numbers and search for a target value using both Linear Search and Binary Search.

## Features

- Enter numbers separated by spaces
- Display the entered numbers
- Perform Linear Search
- Perform Binary Search
- Automatically sort a copy of the list using Insertion Sort before Binary Search
- Display the index of the found number
- Count and display the number of comparisons made
- Menu-driven interface
- Input validation for integer values

## Concepts Practiced

- Functions
- Lists
- Input validation
- List copying (`[:]`)
- Linear Search
- Binary Search
- Insertion Sort
- `while` loops
- Two-pointer technique (`left` and `right`)
- Integer division (`//`)
- Algorithm comparison
- Menu-driven programs

## What I Learned

- Binary Search requires the list to be sorted before searching.
- Creating a copy of the original list allows sorting without changing the user's input.
- Binary Search narrows the search space by repeatedly updating the `left` and `right` boundaries.
- Linear Search checks every element sequentially, while Binary Search eliminates half of the remaining search space in each iteration.
- Tracking the number of comparisons helps compare the efficiency of different searching algorithms.

## Future Improvements

- Let users choose the sorting algorithm before performing Binary Search.
- Display both the original index and the sorted index of the searched element.
- Support searching for duplicate values and display all matching indices.
- Add additional searching algorithms such as Jump Search and Interpolation Search.
- Measure and compare the execution time of Linear Search and Binary Search.
- Store the sorted list to avoid sorting it before every Binary Search.
