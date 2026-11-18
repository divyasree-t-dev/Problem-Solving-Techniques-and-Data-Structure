
# Set 3 - Task 5: Dynamic Programming - Appointment Scheduling

# Appointment data: (Appointment ID, Start Time, End Time)
appointments = [
    ("A101", 9, 11),
    ("A102", 9, 10),
    ("A103", 10, 12),
    ("A104", 11, 13),
    ("A105", 12, 14),
    ("A106", 13, 15),
    ("A107", 14, 16)
]
# Sort appointments by ending time
appointments.sort(key=lambda x: x[2])
# Dynamic Programming approach
def maximum_appointments_dp(appointments):
    n = len(appointments)
    # dp[i] stores the maximum appointments
    # that can be attended among the first i appointments
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        current = appointments[i - 1]
        # Find the last non-overlapping appointment
        previous = 0
        for j in range(i - 2, -1, -1):
            if appointments[j][2] <= current[1]:
                previous = j + 1
                break
        # Include or exclude the current appointment
        include = 1 + dp[previous]
        exclude = dp[i - 1]
        dp[i] = max(include, exclude)
    return dp[n]
# Greedy approach
def maximum_appointments_greedy(appointments):
    count = 0
    last_end_time = 0
    selected = []
    for appointment in appointments:
        if appointment[1] >= last_end_time:
            selected.append(appointment)
            count += 1
            last_end_time = appointment[2]
    return count, selected
# Execute both approaches
dp_result = maximum_appointments_dp(appointments)
greedy_count, greedy_selected = maximum_appointments_greedy(
    appointments
)
print("--- Appointment Scheduling Results ---")
print("Total Appointments:", len(appointments))
print("\nDynamic Programming:")
print("Maximum Appointments:", dp_result)
print("\nGreedy Approach:")
print("Maximum Appointments:", greedy_count)
print("Selected Appointments:")
for appointment in greedy_selected:
    print(
        appointment[0],
        "Start:", appointment[1],
        "End:", appointment[2]
    )
print("\nBoth Approaches Give Same Maximum:",
      dp_result == greedy_count)
