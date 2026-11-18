import time
from collections import deque

# ============================================================
# TASK 1 - BINARY SEARCH TREE
# E-Commerce Product Categories
# ============================================================

class Node:
    def __init__(self, category):
        self.category = category
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, category):
        self.root = self._insert(self.root, category)

    def _insert(self, root, category):
        if root is None:
            return Node(category)

        if category.lower() < root.category.lower():
            root.left = self._insert(root.left, category)
        elif category.lower() > root.category.lower():
            root.right = self._insert(root.right, category)

        return root

    def search(self, category):
        current = self.root

        while current:
            if category.lower() == current.category.lower():
                return True
            elif category.lower() < current.category.lower():
                current = current.left
            else:
                current = current.right

        return False

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.category, end=" -> ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.category, end=" -> ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.category, end=" -> ")


def task1():
    print("\n========== TASK 1: BINARY SEARCH TREE ==========")

    categories = [
        "Electronics", "Clothing", "Books", "Furniture",
        "Beauty", "Sports", "Footwear", "Groceries",
        "Mobiles", "Laptops", "Accessories", "Toys",
        "Home Decor", "Kitchen", "Jewellery"
    ]

    bst = BinarySearchTree()

    for category in categories:
        bst.insert(category)

    print("\n15 Product Categories Inserted Successfully.")

    print("\nInorder Traversal:")
    bst.inorder(bst.root)
    print("END")

    print("\nPreorder Traversal:")
    bst.preorder(bst.root)
    print("END")

    print("\nPostorder Traversal:")
    bst.postorder(bst.root)
    print("END")

    search_category = "Mobiles"

    print("\nSearch Result:")
    if bst.search(search_category):
        print(search_category, "category found.")
    else:
        print(search_category, "category not found.")

    print("\nSearch for Unknown Category:")
    print("Gaming:", "Found" if bst.search("Gaming") else "Not Found")


# ============================================================
# TASK 2 - HASHING AND HASH MAP
# SKU LOOKUP WITH CHAINING
# ============================================================

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return

        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                return item[1]

        return None


def task2():
    print("\n========== TASK 2: HASHING AND HASH MAP ==========")

    hash_table = HashTable(10)

    # Demonstrating collision
    hash_table.insert("SKU-101", "Laptop")
    hash_table.insert("SKU-110", "Mobile")

    print("\nCollision Demonstration:")

    index1 = hash_table.hash_function("SKU-101")
    index2 = hash_table.hash_function("SKU-110")

    print("SKU-101 Hash Index:", index1)
    print("SKU-110 Hash Index:", index2)

    if index1 == index2:
        print("Collision Occurred! Both SKUs are stored using chaining.")

    print("\nCustom Hash Table Lookup:")
    print("SKU-101:", hash_table.search("SKU-101"))
    print("SKU-110:", hash_table.search("SKU-110"))

    # Performance comparison with 100,000 SKUs
    sku_count = 100000

    custom_table = HashTable(200003)
    builtin_map = {}

    print("\nCreating 100,000 SKU Records...")

    for i in range(sku_count):
        sku = f"SKU-{i:06d}"
        product = f"Product-{i}"

        custom_table.insert(sku, product)
        builtin_map[sku] = product

    target_sku = "SKU-099999"

    # Custom hash table lookup
    start = time.perf_counter()

    for _ in range(1000):
        custom_table.search(target_sku)

    custom_time = time.perf_counter() - start

    # Built-in dictionary lookup
    start = time.perf_counter()

    for _ in range(1000):
        builtin_map.get(target_sku)

    builtin_time = time.perf_counter() - start

    print("\nLookup Performance Comparison (1000 searches):")
    print("Total SKUs:", sku_count)
    print("Custom Hash Table Time:", custom_time, "seconds")
    print("Built-in Dictionary Time:", builtin_time, "seconds")

    print("\nLookup Results:")
    print("Custom Hash Table:", custom_table.search(target_sku))
    print("Built-in Dictionary:", builtin_map.get(target_sku))


# ============================================================
# TASK 3 - GRAPH
# MICROSERVICE DEPLOYMENT DEPENDENCIES
# ============================================================

class ServiceGraph:
    def __init__(self):
        self.graph = {}

    def add_service(self, service):
        if service not in self.graph:
            self.graph[service] = []

    def add_dependency(self, service, dependency):
        self.add_service(service)
        self.add_service(dependency)

        # service depends on dependency
        self.graph[dependency].append(service)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        order = []

        while queue:
            service = queue.popleft()
            order.append(service)

            for neighbour in self.graph[service]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return order

    def dfs(self):
        visited = set()
        order = []

        def visit(service):
            visited.add(service)
            order.append(service)

            for neighbour in self.graph[service]:
                if neighbour not in visited:
                    visit(neighbour)

        for service in self.graph:
            if service not in visited:
                visit(service)

        return order

    def detect_cycle(self):
        visited = set()
        recursion_stack = set()

        def check_cycle(service):
            visited.add(service)
            recursion_stack.add(service)

            for neighbour in self.graph[service]:
                if neighbour not in visited:
                    if check_cycle(neighbour):
                        return True
                elif neighbour in recursion_stack:
                    return True

            recursion_stack.remove(service)
            return False

        for service in self.graph:
            if service not in visited:
                if check_cycle(service):
                    return True

        return False


def task3():
    print("\n========== TASK 3: GRAPH ==========")

    graph = ServiceGraph()

    # Deployment dependencies
    graph.add_dependency("cart", "pricing")
    graph.add_dependency("pricing", "inventory")
    graph.add_dependency("cart", "payment")
    graph.add_dependency("payment", "notification")
    graph.add_dependency("notification", "user")

    print("\nMicroservice Dependencies:")
    for service, dependencies in graph.graph.items():
        print(service, "->", dependencies)

    print("\nBFS Deployment Order:")
    print(" -> ".join(graph.bfs("inventory")))

    print("\nDFS Deployment Order:")
    print(" -> ".join(graph.dfs()))

    print("\nCycle Detection:")
    print("Circular Dependency:", graph.detect_cycle())

    # Introduce circular dependency
    graph.add_dependency("inventory", "cart")

    print("\nAfter Adding Circular Dependency:")
    print("Circular Dependency:", graph.detect_cycle())


# ============================================================
# TASK 4 - SLIDING WINDOW
# BUSIEST CONTINUOUS 3-HOUR WINDOW
# ============================================================

def task4():
    print("\n========== TASK 4: SLIDING WINDOW ==========")

    requests = [
        120, 150, 180, 200, 250, 300,
        350, 400, 450, 500, 550, 600,
        650, 700, 750, 800, 850, 900,
        950, 1000, 1100, 1200, 1300, 1400
    ]

    window_size = 3

    current_sum = sum(requests[:window_size])
    max_sum = current_sum
    best_start = 0

    for i in range(window_size, len(requests)):
        current_sum += requests[i]
        current_sum -= requests[i - window_size]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = i - window_size + 1

    print("\nHourly Requests:")
    print(requests)

    print("\nBusiest Continuous 3-Hour Window:")
    print("Starting Hour:", best_start)
    print("Ending Hour:", best_start + 2)
    print("Requests:", requests[best_start:best_start + 3])
    print("Total Requests:", max_sum)


# ============================================================
# TASK 5 - TWO POINTERS
# GIFT CARD VALUE PAIR FINDING
# ============================================================

def task5():
    print("\n========== TASK 5: TWO POINTERS ==========")

    order_values = [
        100, 150, 200, 250, 300,
        350, 400, 450, 500, 550
    ]

    gift_card_value = 600

    left = 0
    right = len(order_values) - 1

    pairs = []

    while left < right:
        current_sum = order_values[left] + order_values[right]

        if current_sum == gift_card_value:
            pairs.append((order_values[left], order_values[right]))
            left += 1
            right -= 1

        elif current_sum < gift_card_value:
            left += 1

        else:
            right -= 1

    print("\nSorted Order Values:")
    print(order_values)

    print("Gift Card Value:", gift_card_value)

    print("\nMatching Pairs:")

    if pairs:
        for first, second in pairs:
            print(first, "+", second, "=", gift_card_value)
    else:
        print("No matching pairs found.")

    print("\nTotal Matching Pairs:", len(pairs))


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("==============================================")
    print(" E-COMMERCE CATALOGUE AND TRAFFIC ANALYSIS")
    print(" DAY 2 - SET 1")
    print("==============================================")

    task1()
    task2()
    task3()
    task4()
    task5()

    print("\n==============================================")
    print(" ALL FIVE TASKS EXECUTED SUCCESSFULLY")
    print("==============================================")
