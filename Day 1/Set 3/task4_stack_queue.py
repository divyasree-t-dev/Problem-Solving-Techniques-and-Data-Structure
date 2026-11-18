
# Set 3 - Task 4: Stack and Queue Implementation

# Queue implementation for walk-in patients
class PatientQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, patient):
        self.queue.append(patient)
    def dequeue(self):
        if not self.queue:
            return "No patients in the queue"
        return self.queue.pop(0)
    def display(self):
        print("Walk-in Patient Queue:", self.queue)
# Stack implementation for recently viewed patients
class PatientHistory:
    def __init__(self):
        self.stack = []
    def push(self, patient):
        self.stack.append(patient)
    def pop(self):
        if not self.stack:
            return "No patient history available"
        return self.stack.pop()
    def display(self):
        print("Recently Viewed Patients:", self.stack)
# Queue demonstration
print("--- Walk-in Patient Queue ---")
walk_in = PatientQueue()
walk_in.enqueue("P1001")
walk_in.enqueue("P1002")
walk_in.enqueue("P1003")
walk_in.display()
print("Patient Served:", walk_in.dequeue())
walk_in.display()
# Stack demonstration
print("\n--- Recently Viewed Patient History ---")
history = PatientHistory()
history.push("P1001")
history.push("P1002")
history.push("P1003")
history.display()
print("Back to Patient:", history.pop())
history.display()
