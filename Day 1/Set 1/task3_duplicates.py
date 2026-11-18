import csv
with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))
# Detect duplicate orders using a dictionary
def detect_duplicates(orders):
    order_groups = {}
    for order in orders:
        key = (
            order["customerId"],
            float(order["amount"]),
            order["createdAt"][:16]
        )
        if key not in order_groups:
            order_groups[key] = []
        order_groups[key].append(order)
    # Keep only groups containing more than one order
    duplicates = {
        key: group
        for key, group in order_groups.items()
        if len(group) > 1
    }
    return duplicates
# Test duplicate detection
duplicates = detect_duplicates(orders)
print("Total orders checked:", len(orders))
print("Duplicate groups found:", len(duplicates))
total_duplicate_orders = sum(
    len(group) for group in duplicates.values()
)
print("Total orders in duplicate groups:", total_duplicate_orders)
# Display a few duplicate groups
for key, group in list(duplicates.items())[:5]:
    print("\nCustomer ID:", key[0])
    print("Amount:", key[1])
    print("Created At:", key[2])
    print("Matching orders:", len(group))
    for order in group:
        print("Order ID:", order["orderId"])
