
# Set 2 - Task 2: Sorting Customer Statements
transactions = [
    {"transactionId": "TXN104", "postingDate": "2026-11-10 10:05:00", "amount": 2500},
    {"transactionId": "TXN102", "postingDate": "2026-11-10 09:30:00", "amount": 1200},
    {"transactionId": "TXN103", "postingDate": "2026-11-10 09:30:00", "amount": 800},
    {"transactionId": "TXN101", "postingDate": "2026-11-10 08:45:00", "amount": 500},
    {"transactionId": "TXN105", "postingDate": "2026-11-10 10:05:00", "amount": 300}
]
# Insertion Sort
def insertion_sort(data):
    arr = data.copy()
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j]["postingDate"] > current["postingDate"]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr
# Merge Sort
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
        # <= preserves original order when dates are equal
        if left[i]["postingDate"] <= right[j]["postingDate"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# Execute both sorting algorithms
insertion_result = insertion_sort(transactions)
merge_result = merge_sort(transactions)
# Display results
print("--- Original Statement ---")
for transaction in transactions:
    print(transaction)
print("\n--- Insertion Sort Result ---")
for transaction in insertion_result:
    print(transaction)
print("\n--- Merge Sort Result ---")
for transaction in merge_result:
    print(transaction)
# Check stability for transactions with the same timestamp
same_timestamp = "2026-11-10 09:30:00"
print("\n--- Stability Check ---")
print("Original order:",
      [t["transactionId"] for t in transactions
       if t["postingDate"] == same_timestamp])
print("Insertion Sort order:",
      [t["transactionId"] for t in insertion_result
       if t["postingDate"] == same_timestamp])
print("Merge Sort order:",
      [t["transactionId"] for t in merge_result
       if t["postingDate"] == same_timestamp])
