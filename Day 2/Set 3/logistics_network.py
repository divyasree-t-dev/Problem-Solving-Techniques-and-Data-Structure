
# ==================================================
# DAY 2 - SET 3
# LOGISTICS NETWORK AND DELIVERY WINDOWS
# ==================================================

# --------------------------------------------------
# TASK 1: BINARY SEARCH TREE
# --------------------------------------------------

class Node:
    def __init__(self, code):
        self.code = code
        self.left = None
        self.right = None

class BST:
    def insert(self, root, code):
        if root is None:
            return Node(code)

        if code < root.code:
            root.left = self.insert(root.left, code)
        elif code > root.code:
            root.right = self.insert(root.right, code)

        return root

    def search(self, root, code):
        if root is None or root.code == code:
            return root

        if code < root.code:
            return self.search(root.left, code)

        return self.search(root.right, code)

    def height(self, root):
        if root is None:
            return -1

        return 1 + max(
            self.height(root.left),
            self.height(root.right)
        )

print("=" * 55)
print("LOGISTICS NETWORK AND DELIVERY WINDOWS")
print("DAY 2 - SET 3")
print("=" * 55)

print("\nTASK 1: BINARY SEARCH TREE")

hub_codes = [50, 30, 70, 20, 40, 60, 80]

bst = BST()
root = None

for code in hub_codes:
    root = bst.insert(root, code)

print("Hub Codes:", hub_codes)

print("Search Hub 40:",
      "Found" if bst.search(root, 40) else "Not Found")

print("Search Hub 90:",
      "Found" if bst.search(root, 90) else "Not Found")

print("Tree Height:", bst.height(root))

sorted_codes = [10, 20, 30, 40, 50]
sorted_root = None

for code in sorted_codes:
    sorted_root = bst.insert(sorted_root, code)

print("Sorted Input:", sorted_codes)
print("Height with Sorted Input:", bst.height(sorted_root))

# --------------------------------------------------
# TASK 2: HASH MAP - PARCEL TRACKING
# --------------------------------------------------

print("\nTASK 2: HASH MAP - PARCEL TRACKING")

parcels = {
    "PK101": "HUB01",
    "PK102": "HUB02",
    "PK103": "HUB01",
    "PK104": "HUB03",
    "PK105": "HUB02"
}

scanned = [
    ("PK101", "HUB01"),
    ("PK102", "HUB02"),
    ("PK103", "HUB01"),
    ("PK101", "HUB01"),
    ("PK104", "HUB03"),
    ("PK102", "HUB02"),
    ("PK105", "HUB02")
]

scan_history = set()

print("\nParcel Tracking Lookup:")

for parcel, hub in scanned:

    if parcel in parcels:
        print(parcel, "->", parcels[parcel])

    scan_key = (parcel, hub)

    if scan_key in scan_history:
        print("Duplicate Scan:", parcel, "at", hub)
    else:
        scan_history.add(scan_key)

# --------------------------------------------------
# TASK 3: GRAPH - BFS AND DFS
# --------------------------------------------------

print("\nTASK 3: LOGISTICS NETWORK GRAPH")

graph = {
    "HUB01": ["HUB02", "HUB03"],
    "HUB02": ["HUB01", "HUB04", "HUB05"],
    "HUB03": ["HUB01", "HUB06"],
    "HUB04": ["HUB02", "HUB07"],
    "HUB05": ["HUB02", "HUB07", "HUB08"],
    "HUB06": ["HUB03", "HUB09"],
    "HUB07": ["HUB04", "HUB05", "HUB10"],
    "HUB08": ["HUB05"],
    "HUB09": ["HUB06"],
    "HUB10": ["HUB07"]
}

# Breadth First Search

from collections import deque

def bfs(graph, start, destination):

    queue = deque([(start, [start])])
    visited = {start}

    while queue:

        current, path = queue.popleft()

        if current == destination:
            return path

        for neighbor in graph[current]:

            if neighbor not in visited:
                visited.add(neighbor)

                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None

# Depth First Search

def dfs(graph, start):

    visited = set()
    stack = [start]
    reachable = []

    while stack:

        current = stack.pop()

        if current not in visited:

            visited.add(current)
            reachable.append(current)

            for neighbor in reversed(graph[current]):

                if neighbor not in visited:
                    stack.append(neighbor)

    return reachable

print("\nAdjacency List:")

for hub, routes in graph.items():
    print(hub, ":", routes)

route = bfs(graph, "HUB01", "HUB10")

if route:
    print("\nShortest Route (BFS):", " -> ".join(route))
    print("Minimum Hops:", len(route) - 1)
else:
    print("No route available")

reachable_hubs = dfs(graph, "HUB01")

print("Reachable Hubs (DFS):", reachable_hubs)

# --------------------------------------------------
# TASK 4: SLIDING WINDOW
# --------------------------------------------------

print("\nTASK 4: DELIVERY WINDOW ANALYSIS")

parcel_counts = [120, 150, 180, 200, 170, 160, 210, 190]

window_size = 4

current_sum = sum(parcel_counts[:window_size])
max_sum = current_sum
max_start = 0

for i in range(window_size, len(parcel_counts)):

    current_sum += parcel_counts[i]
    current_sum -= parcel_counts[i - window_size]

    if current_sum > max_sum:
        max_sum = current_sum
        max_start = i - window_size + 1

best_window = parcel_counts[
    max_start:max_start + window_size
]

average = max_sum / window_size

print("Hourly Parcel Counts:", parcel_counts)
print("Best 4-Hour Window:", best_window)
print("Maximum Parcel Count:", max_sum)
print("Highest Average:", average)

# --------------------------------------------------
# TASK 5: TWO POINTERS - PALINDROME
# --------------------------------------------------

print("\nTASK 5: PALINDROME ROUTE CHECK")


def is_palindrome(route):

    hubs = [
        hub.strip().upper()
        for hub in route.split("->")
    ]

    left = 0
    right = len(hubs) - 1

    while left < right:

        if hubs[left] != hubs[right]:
            return False

        left += 1
        right -= 1

    return True

    
route1 = "HUB01 -> HUB02 -> HUB01"
route2 = "HUB01 -> HUB03 -> HUB02"

print("Route 1:", route1)
print("Is Palindrome:", is_palindrome(route1))

print("Route 2:", route2)
print("Is Palindrome:", is_palindrome(route2))

# --------------------------------------------------
# END OF PROGRAM
# --------------------------------------------------

print("\n" + "=" * 55)
print("ALL 5 TASKS COMPLETED SUCCESSFULLY")
print("=" * 55)