
# Set 3 - Task 3: Double-Booking Detection

# Sample hospital appointments
appointments = [
    {"appointmentId": "A101", "patientId": "P1001", "slot": "09:00"},
    {"appointmentId": "A102", "patientId": "P1002", "slot": "09:30"},
    {"appointmentId": "A103", "patientId": "P1001", "slot": "09:00"},
    {"appointmentId": "A104", "patientId": "P1003", "slot": "10:00"},
    {"appointmentId": "A105", "patientId": "P1002", "slot": "09:30"},
    {"appointmentId": "A106", "patientId": "P1001", "slot": "10:00"},
    {"appointmentId": "A107", "patientId": "P1004", "slot": "11:00"}
]
# Set to track patient and slot combinations
booked_slots = set()
# Store duplicate appointments
duplicates = []
for appointment in appointments:
    key = (
        appointment["patientId"],
        appointment["slot"]
    )
    if key in booked_slots:
        duplicates.append(appointment)
    else:
        booked_slots.add(key)
# Display results
print("Total Appointments Checked:", len(appointments))
print("Unique Patient-Slot Combinations:", len(booked_slots))
print("Double-Booked Appointments Found:", len(duplicates))
print("\n--- Double-Booking Details ---")
for appointment in duplicates:
    print("Appointment ID:", appointment["appointmentId"])
    print("Patient ID:", appointment["patientId"])
    print("Slot:", appointment["slot"])
