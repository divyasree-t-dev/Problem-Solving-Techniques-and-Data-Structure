# Day 1 – Set 2: Retail Banking Transaction Review

## Overview

This project applies Python programming, data structures, and algorithms to a retail banking transaction review system.

The system handles transaction searching, customer statement sorting, duplicate transaction detection, manual review management, and minimum and maximum transaction analysis.

## Tasks Implemented

### 1. Searching Algorithms
- Implemented Linear Search and Binary Search.
- Searched 100,000 sorted transaction IDs.
- Compared the number of comparisons for both algorithms.

### 2. Sorting Customer Statements
- Implemented Insertion Sort and Merge Sort.
- Sorted customer transactions in ascending order based on posting date.
- Compared their time complexity and stability.
- Verified that both algorithms preserve the relative order of transactions with equal timestamps.

### 3. Duplicate Posting Detection
- Used a Python Dictionary (Hash Map).
- Grouped transactions using account number, amount, and merchant name.
- Identified duplicate postings occurring within 60 seconds.

### 4. Stack and Queue Implementation
- Implemented Queue using FIFO for managing the manual review backlog.
- Implemented Stack using LIFO for reversing the most recent banking adjustment.
- Used a front index in the Queue to achieve O(1) dequeue operations.

### 5. Minimum and Maximum Transaction Amount
- Implemented Divide and Conquer and Brute Force approaches.
- Identified the minimum and maximum transaction amounts.
- Compared the number of comparisons and space complexity.

## Technologies Used

- Python 3
- Visual Studio Code
- Python Lists and Dictionaries
- Stack and Queue
- Searching and Sorting Algorithms

## Algorithms and Data Structures

- Linear Search
- Binary Search
- Insertion Sort
- Merge Sort
- Hash Map (Dictionary)
- Stack
- Queue
- Divide and Conquer
- Brute Force

## Performance Results

### Searching Algorithms

| Measurement | Linear Search | Binary Search |
|---|---:|---:|
| Best comparisons | 1 | 1 |
| Average comparisons | 50,000.5 | 15.69 |
| Worst comparisons | 100,000 | 17 |

### Duplicate Detection Results

- Total transactions checked: 6
- Duplicate pairs found: 3
- Duplicate pairs:
  - TXN201 – TXN202
  - TXN201 – TXN204
  - TXN202 – TXN204

### Minimum and Maximum Analysis

| Measurement | Divide and Conquer | Brute Force |
|---|---:|---:|
| Minimum amount | 150 | 150 |
| Maximum amount | 8900 | 8900 |
| Comparisons | 19 | 24 |

## Key Learnings

- Understood the efficiency of Linear Search and Binary Search.
- Learned how stable sorting algorithms help maintain transaction order.
- Applied dictionary-based grouping for duplicate transaction detection.
- Understood Stack and Queue operations in banking applications.
- Compared Divide and Conquer with Brute Force for finding minimum and maximum values.

## Conclusion

This project demonstrates how searching, sorting, hash-based data structures, Stack, Queue, and Divide and Conquer techniques can be applied to banking transaction management. It helped improve understanding of algorithm efficiency and practical problem-solving.
