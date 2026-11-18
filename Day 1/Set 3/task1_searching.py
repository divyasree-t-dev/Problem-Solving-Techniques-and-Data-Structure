
# Set 3 - Task 1: Patient Record Searching
import time
# Generate 20,000 patient records
patients = [
    {"patientId": f"P{100001 + i}", "name": f"Patient_{i + 1}"}
    for i in range(20000)
]
# Linear Search
def linear_search(data, target):
    for patient in data:
        if patient["patientId"] == target:
            return patient
    return None
# Binary Search
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        patient_id = data[mid]["patientId"]
        if patient_id == target:
            return data[mid]
        elif patient_id < target:
            low = mid + 1
        else:
            high = mid - 1
    return None
# Prepare 1,000 lookup targets
lookup_targets = [
    f"P{100001 + (i * 19)}"
    for i in range(1000)
]
# Measure Linear Search time
start_time = time.perf_counter()
for target in lookup_targets:
    linear_search(patients, target)
linear_time = time.perf_counter() - start_time
# Measure Binary Search time
start_time = time.perf_counter()
for target in lookup_targets:
    binary_search(patients, target)
binary_time = time.perf_counter() - start_time
# Display results
print("Total Patient Records:", len(patients))
print("Total Lookups:", len(lookup_targets))
print("\n--- Linear Search ---")
print("Execution Time:", round(linear_time, 6), "seconds")
print("\n--- Binary Search ---")
print("Execution Time:", round(binary_time, 6), "seconds")
print("\n--- Performance Comparison ---")
if binary_time > 0:
    print("Binary Search is approximately",
          round(linear_time / binary_time, 2),
          "times faster than Linear Search.")
# Verify one patient lookup
print("\nSample Patient Search:")
print(binary_search(patients, "P100500"))