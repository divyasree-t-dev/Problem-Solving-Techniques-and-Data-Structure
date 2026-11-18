# Set 2 - Task 1: Searching Algorithms
# Generate 100,000 sorted transaction IDs
transaction_ids = list(range(100001, 200001))
# Linear Search
def linear_search(data, target):
    comparisons = 0
    for transaction_id in data:
        comparisons += 1
        if transaction_id == target:
            return transaction_id, comparisons
    return None, comparisons
# Binary Search
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if data[mid] == target:
            return data[mid], comparisons
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None, comparisons
# Test cases
n = len(transaction_ids)
# Best case
linear_best = linear_search(transaction_ids, transaction_ids[0])[1]
binary_best = binary_search(transaction_ids, transaction_ids[(n-1) // 2])[1]
# Average case (successful searches)
linear_average = (n + 1) / 2
binary_total = sum(
    binary_search(transaction_ids, target)[1]
    for target in transaction_ids
)
binary_average = binary_total / n
# Worst case
linear_worst = linear_search(transaction_ids, transaction_ids[-1])[1]
binary_worst = max(
    binary_search(transaction_ids, target)[1]
    for target in transaction_ids
)
# Display results
print("Total Transaction IDs:", n)
print("\n--- Linear Search ---")
print("Best Case Comparisons:", linear_best)
print("Average Case Comparisons:", round(linear_average, 2))
print("Worst Case Comparisons:", linear_worst)
print("\n--- Binary Search ---")
print("Best Case Comparisons:", binary_best)
print("Average Case Comparisons:", round(binary_average, 2))
print("Worst Case Comparisons:", binary_worst)