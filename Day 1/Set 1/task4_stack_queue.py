class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def is_empty(self):
        return len(self.items) == 0
# Undo Order Edit
order = {"orderId": "100001", "amount": 168.94}
undo_stack = Stack()
# Save the original order before editing
undo_stack.push(order.copy())
# Edit the order
order["amount"] = 200.00
print("After Editing:", order)
# Undo the edit
order = undo_stack.pop()
print("After Undo:", order)
# Queue Implementation
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    def is_empty(self):
        return len(self.items) == 0
# Order Dispatch Line
dispatch_queue = Queue()
dispatch_queue.enqueue("Order 101")
dispatch_queue.enqueue("Order 102")
dispatch_queue.enqueue("Order 103")
print("\nDispatch Queue:", dispatch_queue.items)
print("Dispatched:", dispatch_queue.dequeue())
print("Dispatched:", dispatch_queue.dequeue())
print("Remaining Queue:", dispatch_queue.items)
from collections import deque
# Built-in Stack using List
builtin_stack = []
builtin_stack.append("Edit 1")
builtin_stack.append("Edit 2")
print("\nBuilt-in Stack:", builtin_stack)
print("Undo:", builtin_stack.pop())
# Built-in Queue using Deque
builtin_queue = deque()
builtin_queue.append("Order 101")
builtin_queue.append("Order 102")
builtin_queue.append("Order 103")
print("\nBuilt-in Queue:", list(builtin_queue))
print("Dispatched:", builtin_queue.popleft())
print("Remaining Queue:", list(builtin_queue))