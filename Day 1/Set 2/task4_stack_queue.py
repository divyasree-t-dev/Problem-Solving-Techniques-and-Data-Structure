# Set 2 - Task 4: Stack and Queue
# Queue implementation for manual review backlog
class ReviewQueue:
    def __init__(self):
        self.items = []
        self.front = 0
    def enqueue(self, transaction):
        self.items.append(transaction)
        print("Added to review:", transaction)
    def dequeue(self):
        if self.front >= len(self.items):
            return None
        transaction = self.items[self.front]
        self.front += 1
        return transaction
    def display(self):
        print("Review Queue:", self.items[self.front:])
# Stack implementation for reversing adjustments
class AdjustmentStack:
    def __init__(self):
        self.items = []
    def push(self, adjustment):
        self.items.append(adjustment)
        print("Adjustment applied:", adjustment)
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()
    def display(self):
        print("Adjustment Stack:", self.items)
# Queue demonstration
print("--- Manual Review Queue (FIFO) ---")
review_queue = ReviewQueue()
review_queue.enqueue("TXN301")
review_queue.enqueue("TXN302")
review_queue.enqueue("TXN303")
review_queue.display()
print("Transaction reviewed:", review_queue.dequeue())
print("Transaction reviewed:", review_queue.dequeue())
review_queue.display()
# Stack demonstration
print("\n--- Adjustment Stack (LIFO) ---")
adjustment_stack = AdjustmentStack()
adjustment_stack.push("Adjustment 1: +500")
adjustment_stack.push("Adjustment 2: -200")
adjustment_stack.push("Adjustment 3: +100")
adjustment_stack.display()
print("Reversed adjustment:", adjustment_stack.pop())
print("Reversed adjustment:", adjustment_stack.pop())
adjustment_stack.display()
