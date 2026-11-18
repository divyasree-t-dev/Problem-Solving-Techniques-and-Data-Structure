import csv
# Load orders from CSV
with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))
# Use the first 10,000 records for comparison
sample_orders = orders[:10000]
# Bubble Sort - Descending order
def bubble_sort(data):
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if float(arr[j]["amount"]) < float(arr[j + 1]["amount"]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Test with a small sample first
small_sample = sample_orders[:5]
result = bubble_sort(small_sample)
print("Original amounts:",
      [order["amount"] for order in small_sample])
print("Bubble Sort (Descending):",
      [order["amount"] for order in result])

# Merge Sort - Descending order
def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if float(left[i]["amount"]) >= float(right[j]["amount"]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test Merge Sort
merge_result = merge_sort(small_sample)
print("Merge Sort (Descending):",
      [order["amount"] for order in merge_result])
import time
print("\n--- Sorting Performance (10,000 Records) ---")
# Bubble Sort timing
start = time.perf_counter()
bubble_result = bubble_sort(sample_orders)
bubble_time = time.perf_counter() - start
# Merge Sort timing
start = time.perf_counter()
merge_result = merge_sort(sample_orders)
merge_time = time.perf_counter() - start
# Built-in Sort timing
start = time.perf_counter()
builtin_result = sorted(
    sample_orders,
    key=lambda order: float(order["amount"]),
    reverse=True
)
builtin_time = time.perf_counter() - start
print("Bubble Sort Time:", round(bubble_time, 4), "seconds")
print("Merge Sort Time:", round(merge_time, 4), "seconds")
print("Built-in Sort Time:", round(builtin_time, 4), "seconds")
# Verify all sorting results
print("Bubble Sort Correct:", 
      [x["amount"] for x in bubble_result] ==
      [x["amount"] for x in builtin_result])
print("Merge Sort Correct:",
      [x["amount"] for x in merge_result] ==
      [x["amount"] for x in builtin_result])