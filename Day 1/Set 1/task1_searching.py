import csv
import time
with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))
print("Total orders:", len(orders))
print("First order:", orders[0])
def linear_search(orders, target_id):
    for order in orders:
        if order["orderId"] == target_id:
            return order
    return None
# Test linear search
result = linear_search(orders, "100001")
print("Linear Search Result:", result)
# Sort orders by orderId
sorted_orders = sorted(orders, key=lambda order: int(order["orderId"]))
def binary_search(orders, target_id):
    low = 0
    high = len(orders) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_id = int(orders[mid]["orderId"])
        if mid_id == target_id:
            return orders[mid]
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None
# Test binary search
result = binary_search(sorted_orders, 100001)
print("Binary Search Result:", result)
# Benchmark both searching algorithms
target_id = orders[-1]["orderId"]
iterations = 100
# Linear Search timing
start = time.perf_counter()
for _ in range(iterations):
    linear_search(orders, target_id)
linear_time = time.perf_counter() - start
# Binary Search timing
start = time.perf_counter()
for _ in range(iterations):
    binary_search(sorted_orders, int(target_id))
binary_time = time.perf_counter() - start
print("\n--- Search Performance ---")
print("Target Order ID:", target_id)
print("Linear Search Average Time:",
      (linear_time / iterations) * 1000, "ms")
print("Binary Search Average Time:",
      (binary_time / iterations) * 1000, "ms")