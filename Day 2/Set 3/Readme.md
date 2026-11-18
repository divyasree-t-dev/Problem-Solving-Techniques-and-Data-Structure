# Day 2 – Set 3: Logistics Network and Delivery Windows

## Overview

This project implements data structures and algorithms to optimise hub-to-hub routing, parcel tracking, and delivery-window planning for a courier company.

The implementation covers Binary Search Trees, Hash Maps, Graph Traversal, Sliding Window, and Two-Pointer techniques using Python.

## Technologies Used

- Python 3
- Binary Search Tree (BST)
- Hash Map and Set
- Graph (Adjacency List)
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Sliding Window
- Two Pointers

## Tasks Implemented

### Task 1: Binary Search Tree

- Stored hub codes in a Binary Search Tree.
- Implemented insertion and search operations.
- Calculated the height of the BST.
- Demonstrated the effect of sorted input on tree height.

**Result:**
- Hub 40: Found
- Hub 90: Not Found
- Balanced tree height: 2
- Sorted input tree height: 4

### Task 2: Hash Map – Parcel Tracking

- Created a hash map to store parcel tracking numbers and their associated hubs.
- Implemented parcel lookup.
- Used a set to track parcel scans.
- Detected duplicate scans when the same parcel was scanned again at the same hub.

**Result:**
- Duplicate scan detected: PK101 at HUB01
- Duplicate scan detected: PK102 at HUB02

### Task 3: Logistics Network Graph

- Represented 10 logistics hubs using an adjacency list.
- Implemented Breadth First Search (BFS) to find the shortest route.
- Implemented Depth First Search (DFS) to identify all reachable hubs from the central depot.

**Shortest Route:**

HUB01 → HUB02 → HUB04 → HUB07 → HUB10

**Minimum Hops:** 4

**Reachable Hubs:** All 10 hubs are reachable from HUB01.

### Task 4: Sliding Window – Delivery Window Analysis

- Used hourly parcel counts as input.
- Applied the sliding window technique to examine consecutive 4-hour periods.
- Identified the window with the highest parcel count and average.

**Input:** [120, 150, 180, 200, 170, 160, 210, 190]

**Best 4-Hour Window:** [200, 170, 160, 210]

**Maximum Parcel Count:** 740

**Highest Average:** 185.0

### Task 5: Two Pointers – Palindrome Route Check

- Implemented the two-pointer technique to verify palindrome routes.
- Compared hub codes from both ends.
- Ignored case differences and route separators.

**Results:**
- HUB01 → HUB02 → HUB01: True
- HUB01 → HUB03 → HUB02: False

## Algorithm Complexity

| Algorithm | Time Complexity |
|---|---|
| BST Insertion | O(h) |
| BST Search | O(h) |
| BST Height Calculation | O(n) |
| Hash Map Lookup | O(1) Average |
| Duplicate Scan Detection | O(1) Average |
| BFS | O(V + E) |
| DFS | O(V + E) |
| Sliding Window | O(n) |
| Two Pointers | O(n) |

## How to Run

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Execute the following command:

```bash
python logistics_network.py
```

## Project Structure

```text
Set_3/
│
├── logistics_network.py
└── README.md
```

## Conclusion

This project demonstrates the practical application of fundamental data structures and problem-solving techniques in logistics operations. It provides efficient parcel tracking, route identification, delivery-window analysis, and palindrome verification using Python.
