# Set 2 - Task 5: Find Minimum and Maximum
transaction_amounts = [
    4500, 1200, 7800, 300, 6500,
    900, 2500, 8900, 150, 5200,
    1100, 7200, 400
]
# Divide and Conquer approach
def find_min_max(data, low, high):
    global dc_comparisons
    # Only one element
    if low == high:
        return data[low], data[low]
    # Two elements
    if high == low + 1:
        dc_comparisons += 1
        if data[low] < data[high]:
            return data[low], data[high]
        else:
            return data[high], data[low]
    # Divide the array into two halves
    mid = (low + high) // 2
    left_min, left_max = find_min_max(data, low, mid)
    right_min, right_max = find_min_max(data, mid + 1, high)
    # Combine the results
    dc_comparisons += 2
    minimum = min(left_min, right_min)
    maximum = max(left_max, right_max)
    return minimum, maximum
# Brute Force approach
def brute_force_min_max(data):
    global bf_comparisons
    minimum = data[0]
    maximum = data[0]
    for amount in data[1:]:
        bf_comparisons += 2
        if amount < minimum:
            minimum = amount
        if amount > maximum:
            maximum = amount
    return minimum, maximum
# Execute Divide and Conquer
dc_comparisons = 0
dc_min, dc_max = find_min_max(
    transaction_amounts, 0, len(transaction_amounts) - 1
)
# Execute Brute Force
bf_comparisons = 0
bf_min, bf_max = brute_force_min_max(transaction_amounts)
# Display results
print("Total Transactions:", len(transaction_amounts))
print("\n--- Divide and Conquer ---")
print("Minimum Amount:", dc_min)
print("Maximum Amount:", dc_max)
print("Comparisons:", dc_comparisons)
print("\n--- Brute Force ---")
print("Minimum Amount:", bf_min)
print("Maximum Amount:", bf_max)
print("Comparisons:", bf_comparisons)
print("\n--- Result Comparison ---")
print("Both methods give the same result:",
      dc_min == bf_min and dc_max == bf_max)
