
# Day 2 - Set 2: Insurance Claims Processing

## Overview

This project implements different data structures and problem-solving techniques for an insurance claims processing system.

The system helps manage insurance claim IDs, identify duplicate submissions, model claim approval workflows, detect claim spikes, and merge sorted claim records from regional offices.

## Business Scenario

An insurance company needs an efficient system to process claims through different approval stages. It must identify duplicate claims, monitor unusual increases in claim submissions, and combine records from multiple regional offices.

## Technologies Used

- Python 3
- Visual Studio Code
- Data Structures and Algorithms

## Tasks Implemented

### Task 1: Binary Search Tree (BST)

- Created a Binary Search Tree to store claim IDs.
- Implemented insertion and searching operations.
- Implemented Inorder, Preorder, and Postorder traversals.
- Inorder traversal displays claim IDs in ascending sorted order.

### Task 2: Hashing and Duplicate Detection

- Used Python dictionaries for hashing.
- Normalized policy numbers by removing spaces and ignoring letter case.
- Compared policy numbers and incident dates to identify duplicate claims.
- Python dictionaries internally handle hash collisions using their built-in collision resolution mechanisms.

### Task 3: Graph – Claim Approval Workflow

- Represented claim approval stages as a directed graph.
- Implemented Breadth-First Search (BFS) to find the shortest path.
- Implemented Depth-First Search (DFS) to detect cycles.
- Approval stages include:
  - Registration
  - Assessment
  - Surveyor
  - Settlement

### Task 4: Sliding Window – Claim Spike Detection

- Used the sliding window technique to identify consecutive days with more than 100 claims.
- Calculated the longest consecutive run of claim spikes.
- Returned the length and day positions of the longest run.

### Task 5: Two Pointers – Merging Regional Claims

- Used two pointers to merge two sorted claim lists.
- Combined records from two regional offices.
- Maintained ascending order without performing an additional sorting operation.

## Project Structure

```text
Set_2_Insurance_Claims/
│
├── main.py
└── README.md
```

## How to Run

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Execute the following command:

```bash
python main.py
```

4. The program executes all five tasks and displays their outputs.
5. Test cases are also executed to verify empty inputs and duplicate handling.

## Test Cases

| Test Case | Expected Behaviour |
|---|---|
| Empty BST | Returns an empty traversal |
| Duplicate BST insertion | Rejects duplicate claim ID |
| Search existing claim | Returns True |
| Search missing claim | Returns False |
| Empty claim list | Returns no duplicates |
| Duplicate policy and date | Identifies duplicate claims |
| Empty graph | Returns no path and no cycle |
| Graph with a cycle | Detects the cycle |
| Empty sliding window | Returns zero consecutive days |
| No claims above 100 | Returns zero |
| Empty regional lists | Returns an empty merged list |
| Duplicate values in sorted lists | Merges while preserving duplicates |

## Time and Space Complexity Analysis

Let:
- n = Number of claim records.
- h = Height of the Binary Search Tree.
- V = Number of graph vertices.
- E = Number of graph edges.

| Task | Operation | Time Complexity | Space Complexity |
|---|---|---|---|
| BST | Insert | O(h) | O(1) auxiliary |
| BST | Search | O(h) | O(1) |
| BST | Traversals | O(n) | O(h) |
| Hashing | Duplicate Detection | O(n) average | O(n) |
| Graph | BFS | O(V + E) | O(V) |
| Graph | DFS Cycle Detection | O(V + E) | O(V) |
| Sliding Window | Spike Detection | O(n) | O(n) for returned positions |
| Two Pointers | Merge Sorted Lists | O(n + m) | O(n + m) |

Note: A BST can take O(n) time for insertion and searching in the worst case when it becomes skewed. Hashing operations are O(1) on average, but can degrade in collision-heavy cases.

## Conclusion

The Insurance Claims Processing project demonstrates the practical application of Binary Search Trees, Hashing, Graph Traversal, Sliding Window, and Two-Pointer techniques.

These techniques help improve claim record management, duplicate detection, approval workflow analysis, claim spike monitoring, and regional data merging.

All five tasks are implemented and tested using Python.
