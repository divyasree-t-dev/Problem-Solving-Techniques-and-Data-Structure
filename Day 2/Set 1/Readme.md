# Day 2 – Problem Solving Techniques and Data Structures – II

## Set 1 – E-Commerce Catalogue and Traffic Analysis

### Overview

This assignment focuses on implementing different data structures and problem-solving techniques for an e-commerce platform.

The objective is to improve product category management, SKU searching, microservice dependency analysis, traffic monitoring and gift-card order matching.

**Programming Language:** Python 3.12

### Tasks Implemented

#### 1. Binary Search Tree (BST)
- Created a Binary Search Tree with 15 product categories.
- Implemented insertion and searching operations.
- Performed inorder, preorder and postorder traversals.
- Verified existing and non-existing category searches.

#### 2. Hashing and HashMap
- Implemented a custom hash table using chaining.
- Demonstrated hash collisions using sample SKUs.
- Created 100,000 SKU records.
- Compared lookup performance between a custom hash table and Python's built-in dictionary.
- Measured lookup time using `time.perf_counter()`.

#### 3. Graph – Microservice Dependencies
- Modelled microservice dependencies using an adjacency list.
- Implemented Breadth-First Search (BFS).
- Implemented Depth-First Search (DFS).
- Detected circular dependencies using DFS and a recursion stack.

#### 4. Sliding Window
- Used 24 hourly request values.
- Implemented a sliding window of size three.
- Identified the busiest continuous three-hour window.
- Calculated the maximum total number of requests.

#### 5. Two-Pointer Technique
- Used a sorted list of order values.
- Implemented the two-pointer approach.
- Identified all pairs matching the gift-card value of 600.

### Technologies Used

- Python 3.12
- Visual Studio Code
- Built-in Python modules:
  - `time`
  - `collections.deque`

### Project Structure

```text
Set-1/
│
├── main.py
├── output.docx
└── README.md
```

### How to Execute

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Execute the following command:

```bash
python main.py
```

No external libraries are required.

### Execution Results

All five tasks were executed successfully.

| Task | Result |
|---|---|
| Binary Search Tree | 15 categories inserted and traversals completed |
| Hashing and HashMap | Collision demonstrated and 100,000 SKU lookups compared |
| Graph | BFS, DFS and circular dependency detection completed |
| Sliding Window | Busiest 3-hour window identified with 3,900 requests |
| Two Pointers | Four matching pairs identified |

### Decision Table

| Problem | Data Structure / Pattern | Reason |
|---|---|---|
| Category management | Binary Search Tree | Organized insertion and searching |
| SKU lookup | Hash Table with Chaining | Efficient lookup and collision handling |
| SKU performance comparison | HashMap / Dictionary | Fast key-value access |
| Microservice dependencies | Graph | Represents service relationships |
| Graph traversal | BFS and DFS | Explores connected services |
| Cycle detection | DFS with Recursion Stack | Identifies circular dependencies |
| Traffic analysis | Sliding Window | Finds maximum consecutive request totals |
| Gift-card matching | Two Pointers | Efficiently finds matching pairs |

### Conclusion

This assignment provided practical experience in implementing fundamental data structures and algorithms using Python.

All five tasks were successfully completed and their execution results are documented in `output.docx`.

