
# Set 3 - Task 2: Appointment Sorting

import time
# Sample hospital appointments
appointments = [
    {"patientId": "P105", "urgency": 3, "arrivalTime": "09:30"},
    {"patientId": "P102", "urgency": 1, "arrivalTime": "09:15"},
    {"patientId": "P104", "urgency": 2, "arrivalTime": "08:45"},
    {"patientId": "P101", "urgency": 1, "arrivalTime": "08:30"},
    {"patientId": "P103", "urgency": 3, "arrivalTime": "08:50"},
    {"patientId": "P106", "urgency": 2, "arrivalTime": "09:00"}
]
# Sorting key:
# Lower urgency number means higher priority.
def sort_key(appointment):
    return (appointment["urgency"], appointment["arrivalTime"])
# Selection Sort
def selection_sort(data):
    arr = data.copy()
    swaps = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if sort_key(arr[j]) < sort_key(arr[min_index]):
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return arr, swaps
# Quick Sort
def quick_sort(data):
    arr = data.copy()
    swaps = 0
    def partition(low, high):
        nonlocal swaps
        pivot = sort_key(arr[high])
        i = low - 1
        for j in range(low, high):
            if sort_key(arr[j]) <= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps += 1
        return i + 1
    def quick_sort_recursive(low, high):
        if low < high:
            pivot_index = partition(low, high)
            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)
    quick_sort_recursive(0, len(arr) - 1)
    return arr, swaps
# Run Selection Sort and measure time
start = time.perf_counter()
selection_result, selection_swaps = selection_sort(appointments)
selection_time = time.perf_counter() - start
# Run Quick Sort and measure time
start = time.perf_counter()
quick_result, quick_swaps = quick_sort(appointments)
quick_time = time.perf_counter() - start
# Display original appointments
print("--- Original Appointments ---")
for appointment in appointments:
    print(appointment)
# Display Selection Sort result
print("\n--- Selection Sort Result ---")
for appointment in selection_result:
    print(appointment)
print("Selection Sort Swaps:", selection_swaps)
print("Selection Sort Time:", round(selection_time, 8), "seconds")
# Display Quick Sort result
print("\n--- Quick Sort Result ---")
for appointment in quick_result:
    print(appointment)
print("Quick Sort Swaps:", quick_swaps)
print("Quick Sort Time:", round(quick_time, 8), "seconds")
# Verify both results
print("\nBoth algorithms give the same result:",
      selection_result == quick_result)
