
# ============================================================
# DAY 2 - SET 2: INSURANCE CLAIMS PROCESSING
# Topics: BST, Hashing, Graphs, Sliding Window, Two Pointers
# ============================================================


# -------------------- TASK 1: BINARY SEARCH TREE --------------------

class BSTNode:
    def __init__(self, claim_id):
        self.claim_id = claim_id
        self.left = None
        self.right = None


class ClaimBST:
    def __init__(self):
        self.root = None

    def insert(self, claim_id):
        if self.root is None:
            self.root = BSTNode(claim_id)
            return True

        current = self.root

        while True:
            if claim_id == current.claim_id:
                return False

            elif claim_id < current.claim_id:
                if current.left is None:
                    current.left = BSTNode(claim_id)
                    return True
                current = current.left

            else:
                if current.right is None:
                    current.right = BSTNode(claim_id)
                    return True
                current = current.right

    def search(self, claim_id):
        current = self.root

        while current:
            if current.claim_id == claim_id:
                return True
            elif claim_id < current.claim_id:
                current = current.left
            else:
                current = current.right

        return False

    def inorder(self, node):
        if node is None:
            return []

        return (self.inorder(node.left) +
                [node.claim_id] +
                self.inorder(node.right))

    def preorder(self, node):
        if node is None:
            return []

        return ([node.claim_id] +
                self.preorder(node.left) +
                self.preorder(node.right))

    def postorder(self, node):
        if node is None:
            return []

        return (self.postorder(node.left) +
                self.postorder(node.right) +
                [node.claim_id])


# -------------------- TASK 2: HASHING --------------------

def normalize_claim(policy_number, incident_date):
    normalized_policy = "".join(policy_number.split()).casefold()
    normalized_date = incident_date.strip()

    return normalized_policy, normalized_date


def detect_duplicates(claims):
    claim_map = {}
    duplicates = []

    for claim in claims:
        key = normalize_claim(
            claim["policy_number"],
            claim["incident_date"]
        )

        if key in claim_map:
            duplicates.append({
                "original_claim": claim_map[key],
                "duplicate_claim": claim["claim_id"]
            })
        else:
            claim_map[key] = claim["claim_id"]

    return duplicates


# -------------------- TASK 3: GRAPH --------------------

class ClaimApprovalGraph:
    def __init__(self):
        self.graph = {}

    def add_stage(self, stage):
        if stage not in self.graph:
            self.graph[stage] = []

    def add_transition(self, source, destination):
        self.add_stage(source)
        self.add_stage(destination)

        if destination not in self.graph[source]:
            self.graph[source].append(destination)

    # BFS - Shortest path
    def shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return []

        queue = [(start, [start])]
        visited = {start}

        while queue:
            current, path = queue.pop(0)

            if current == end:
                return path

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return []

    # DFS - Cycle detection
    def has_cycle(self):
        visited = set()
        recursion_stack = set()

        def dfs(node):
            visited.add(node)
            recursion_stack.add(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

                elif neighbor in recursion_stack:
                    return True

            recursion_stack.remove(node)
            return False

        for node in self.graph:
            if node not in visited:
                if dfs(node):
                    return True

        return False


# -------------------- TASK 4: SLIDING WINDOW --------------------

def longest_claim_spike(claim_counts, threshold=100):
    max_length = 0
    current_length = 0
    start_index = -1
    best_start = -1

    for i, count in enumerate(claim_counts):
        if count > threshold:
            current_length += 1

            if current_length == 1:
                start_index = i

            if current_length > max_length:
                max_length = current_length
                best_start = start_index

        else:
            current_length = 0

    if max_length == 0:
        return 0, []

    days = list(range(best_start + 1, best_start + max_length + 1))

    return max_length, days


# -------------------- TASK 5: TWO POINTERS --------------------

def merge_claim_lists(region_a, region_b):
    i = 0
    j = 0
    merged = []

    while i < len(region_a) and j < len(region_b):

        if region_a[i] <= region_b[j]:
            merged.append(region_a[i])
            i += 1
        else:
            merged.append(region_b[j])
            j += 1

    merged.extend(region_a[i:])
    merged.extend(region_b[j:])

    return merged


# ==================== MAIN PROGRAM ====================

def main():

    print("=" * 55)
    print(" DAY 2 - SET 2: INSURANCE CLAIMS PROCESSING")
    print("=" * 55)

    # TASK 1
    print("\n========== TASK 1: BINARY SEARCH TREE ==========")

    bst = ClaimBST()

    claim_ids = [105, 102, 108, 101, 104, 107, 110]

    for claim_id in claim_ids:
        bst.insert(claim_id)

    print("Claim IDs Inserted:", claim_ids)
    print("Inorder Traversal:", bst.inorder(bst.root))
    print("Preorder Traversal:", bst.preorder(bst.root))
    print("Postorder Traversal:", bst.postorder(bst.root))
    print("Search Claim 104:", bst.search(104))
    print("Search Claim 999:", bst.search(999))

    print("Explanation: Inorder traversal gives claim IDs in sorted order.")

    # TASK 2
    print("\n========== TASK 2: HASHING ==========")

    claims = [
        {
            "claim_id": "CL101",
            "policy_number": "POL123",
            "incident_date": "2026-11-01"
        },
        {
            "claim_id": "CL102",
            "policy_number": "pol123",
            "incident_date": "2026-11-01"
        },
        {
            "claim_id": "CL103",
            "policy_number": "POL 456",
            "incident_date": "2026-11-02"
        },
        {
            "claim_id": "CL104",
            "policy_number": "pol456",
            "incident_date": "2026-11-02"
        },
        {
            "claim_id": "CL105",
            "policy_number": "POL789",
            "incident_date": "2026-11-03"
        }
    ]

    duplicates = detect_duplicates(claims)

    print("Total Claims:", len(claims))
    print("Duplicate Claims:")

    if duplicates:
        for item in duplicates:
            print(
                item["original_claim"],
                "->",
                item["duplicate_claim"]
            )
    else:
        print("No duplicates found.")

    print("Collision Handling: Python dictionaries handle hash collisions internally.")

    # TASK 3
    print("\n========== TASK 3: GRAPH ==========")

    approval_graph = ClaimApprovalGraph()

    stages = [
        "Registration",
        "Assessment",
        "Surveyor",
        "Settlement"
    ]

    for stage in stages:
        approval_graph.add_stage(stage)

    approval_graph.add_transition("Registration", "Assessment")
    approval_graph.add_transition("Assessment", "Surveyor")
    approval_graph.add_transition("Surveyor", "Settlement")
    approval_graph.add_transition("Assessment", "Settlement")

    print("Approval Stages:", stages)

    path = approval_graph.shortest_path(
        "Registration",
        "Settlement"
    )

    print("Shortest Approval Path:", " -> ".join(path))
    print("Cycle Detected:", approval_graph.has_cycle())

    # Demonstrate cycle detection
    approval_graph.add_transition("Settlement", "Assessment")

    print("Cycle After Adding Reverse Transition:",
          approval_graph.has_cycle())

    # TASK 4
    print("\n========== TASK 4: SLIDING WINDOW ==========")

    daily_claims = [85, 120, 135, 150, 90, 115, 125, 140, 80, 105]

    length, days = longest_claim_spike(daily_claims)

    print("Daily Claim Counts:", daily_claims)
    print("Longest Consecutive Spike:", length, "days")
    print("Day Positions:", days)

    # TASK 5
    print("\n========== TASK 5: TWO POINTERS ==========")

    region_a = [101, 104, 108, 112, 120]
    region_b = [102, 105, 109, 115, 118]

    merged_claims = merge_claim_lists(region_a, region_b)

    print("Region A Claims:", region_a)
    print("Region B Claims:", region_b)
    print("Merged Sorted Claims:", merged_claims)

    # ==================== TEST CASES ====================

    print("\n========== TEST CASES ==========")

    # BST empty input and duplicate
    empty_bst = ClaimBST()

    print("Empty BST Traversal:", empty_bst.inorder(empty_bst.root))
    print("Empty BST Search:", empty_bst.search(100))
    print("Duplicate BST Insertion:", bst.insert(105))

    # Hashing empty input and duplicate
    print("Empty Claims:", detect_duplicates([]))
    print("Duplicate Detection:", len(duplicates) == 2)

    # Graph empty input and unreachable path
    empty_graph = ClaimApprovalGraph()

    print("Empty Graph Path:",
          empty_graph.shortest_path("A", "B"))
    print("Empty Graph Cycle:", empty_graph.has_cycle())

    # Sliding window empty and no spike
    print("Empty Sliding Window:",
          longest_claim_spike([]))
    print("No Spike:",
          longest_claim_spike([20, 50, 80]))

    # Two pointers empty and duplicate values
    print("Empty Merge:",
          merge_claim_lists([], []))

    print("Merge with Duplicates:",
          merge_claim_lists([101, 103], [101, 102, 103]))

    print("\n" + "=" * 55)
    print(" ALL TASKS COMPLETED SUCCESSFULLY")
    print("=" * 55)


if __name__ == "__main__":
    main()
