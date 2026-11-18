# Day 1 – Set 1: Retail Order Desk

## Overview

This project implements fundamental problem-solving techniques and data structures using Python for an online retail order management system.

The system handles order searching, sorting, duplicate detection, order editing, dispatch management, and refund calculation.

## Tasks Implemented

### 1. Searching Algorithms
- Implemented Linear Search and Binary Search.
- Searched 50,003 order records.
- Compared execution time over 100 iterations.

### 2. Sorting Algorithms
- Implemented Bubble Sort and Merge Sort.
- Compared both algorithms with Python's built-in sorting method.
- Sorted 10,000 orders by amount in descending order.
- Traced the first three passes of Bubble Sort.

### 3. Duplicate Order Detection
- Used a Python Dictionary (Hash Map).
- Identified duplicate orders using customer ID, amount, and creation time within the same minute.
- Detected duplicate order groups efficiently.

### 4. Stack and Queue Implementation
- Implemented Stack using the LIFO principle for undoing order edits.
- Implemented Queue using the FIFO principle for order dispatching.
- Compared list-based implementations with Python's built-in data structures.

### 5. Greedy Algorithm and Dynamic Programming
- Calculated the minimum number of currency notes and coins required for refunds.
- Compared Greedy and Dynamic Programming approaches.
- Demonstrated a Greedy failure case using denominations 4, 3, and 1.

## Technologies Used

- Python 3
- Visual Studio Code
- CSV
- Python Collections
- Data Structures and Algorithms

## Algorithms and Data Structures

- Linear Search
- Binary Search
- Bubble Sort
- Merge Sort
- Python Built-in Sort
- Hash Map (Dictionary)
- Stack
- Queue
- Greedy Algorithm
- Dynamic Programming

## Performance Results

| Algorithm | Execution Time |
|---|---:|
| Linear Search | 29.3617 ms |
| Binary Search | 0.008895 ms |
| Bubble Sort | 345.0455 seconds |
| Merge Sort | 0.6273 seconds |
| Python Built-in Sort | 0.0443 seconds |

## Duplicate Detection Results

- Total orders checked: 50,003
- Duplicate groups found: 3
- Total orders in duplicate groups: 6

## Greedy vs Dynamic Programming

**Refund amount:** ₹786

- Greedy approach: 7 notes/coins.

**Greedy failure example:**

- Denominations: 4, 3, 1
- Amount: 6
- Greedy result: 3 coins (4 + 1 + 1)
- Dynamic Programming result: 2 coins (3 + 3)

## Key Learnings

- Understood the performance differences between Linear Search and Binary Search.
- Learned how sorting algorithms work and how their execution times differ.
- Applied hash-based data structures for efficient duplicate detection.
- Understood LIFO and FIFO principles through Stack and Queue.
- Learned the differences between Greedy and Dynamic Programming approaches.

## Conclusion

This project demonstrates the practical application of algorithms and data structures in retail order management. It helped develop problem-solving skills and understand how different techniques improve the efficiency of real-world applications.
