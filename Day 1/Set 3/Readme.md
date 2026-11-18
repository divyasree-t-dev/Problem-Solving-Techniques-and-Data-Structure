# Day 1 – Set 3: Hospital Appointment Desk

## Overview

This project applies Python programming, data structures, and algorithms to a hospital appointment management system.

The system handles patient record searching, appointment sorting, double-booking detection, walk-in patient management, patient history tracking, and appointment scheduling.

## Tasks Implemented

### 1. Searching Algorithms
- Implemented Linear Search and Binary Search.
- Searched 20,000 patient records.
- Compared the execution time of both algorithms using 1,000 lookups.

### 2. Appointment Sorting
- Implemented Selection Sort and Quick Sort.
- Sorted appointments based on urgency and arrival time.
- Prioritized appointments with lower urgency numbers.
- Used earlier arrival time when two appointments had the same urgency.

### 3. Double-Booking Detection
- Used a Python Set (Hash Set).
- Identified duplicate appointments using patient ID and appointment slot.
- Detected repeated patient bookings for the same time slot.

### 4. Stack and Queue Implementation
- Implemented Queue using FIFO for managing walk-in patient tokens.
- Implemented Stack using LIFO for managing recently viewed patient history.
- Demonstrated insertion and removal operations.

### 5. Appointment Scheduling
- Implemented Greedy Algorithm and Dynamic Programming.
- Selected the maximum number of non-overlapping appointments within a hospital shift.
- Compared both approaches based on their scheduling results and efficiency.

## Technologies Used

- Python 3
- Visual Studio Code
- Python Lists and Sets
- Stack and Queue
- Searching and Sorting Algorithms
- Greedy Algorithm
- Dynamic Programming

## Algorithms and Data Structures

- Linear Search
- Binary Search
- Selection Sort
- Quick Sort
- Hash Set
- Stack
- Queue
- Greedy Algorithm
- Dynamic Programming

## Performance Results

### Searching Algorithms

| Algorithm | Execution Time |
|---|---:|
| Linear Search | 3.811007 seconds |
| Binary Search | 0.036001 seconds |

Binary Search was approximately 105.86 times faster than Linear Search in the tested experiment.

### Appointment Sorting Results

| Algorithm | Execution Time | Swaps |
|---|---:|---:|
| Selection Sort | 0.0000299 seconds | 2 |
| Quick Sort | 0.0003292 seconds | 6 |

Both algorithms produced the same appointment order based on urgency and arrival time.

### Double-Booking Detection

- Total appointments checked: 7
- Unique patient-slot combinations: 5
- Duplicate appointments: 2

### Appointment Scheduling Results

- Total appointments: 7
- Maximum non-overlapping appointments selected: 4
- Both Greedy and Dynamic Programming selected the same appointments:
  - A102 (09:00–10:00)
  - A103 (10:00–12:00)
  - A105 (12:00–14:00)
  - A107 (14:00–16:00)

## Key Learnings

- Understood the performance differences between Linear Search and Binary Search.
- Learned how Selection Sort and Quick Sort arrange appointments based on multiple conditions.
- Applied Hash Set for detecting double-booked appointments.
- Understood FIFO and LIFO principles through Queue and Stack.
- Compared Greedy and Dynamic Programming approaches for appointment scheduling.

## Conclusion

This project demonstrates how algorithms and data structures can be applied to hospital appointment management. It helped develop practical problem-solving skills in patient searching, appointment prioritization, duplicate detection, patient management, and scheduling optimization.
