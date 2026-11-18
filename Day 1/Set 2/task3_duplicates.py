# Set 2 - Task 3: Duplicate Posting Detection
from datetime import datetime
# Sample banking transactions
transactions = [
    {
        "transactionId": "TXN201",
        "account": "ACC101",
        "amount": 1500,
        "merchant": "Amazon",
        "timestamp": "2026-11-10 10:00:00"
    },
    {
        "transactionId": "TXN202",
        "account": "ACC101",
        "amount": 1500,
        "merchant": "Amazon",
        "timestamp": "2026-11-10 10:00:30"
    },
    {
        "transactionId": "TXN203",
        "account": "ACC102",
        "amount": 2500,
        "merchant": "Flipkart",
        "timestamp": "2026-11-10 10:05:00"
    },
    {
        "transactionId": "TXN204",
        "account": "ACC101",
        "amount": 1500,
        "merchant": "Amazon",
        "timestamp": "2026-11-10 10:00:45"
    },
    {
        "transactionId": "TXN205",
        "account": "ACC103",
        "amount": 500,
        "merchant": "Amazon",
        "timestamp": "2026-11-10 10:10:00"
    },
    {
        "transactionId": "TXN206",
        "account": "ACC102",
        "amount": 2500,
        "merchant": "Flipkart",
        "timestamp": "2026-11-10 10:08:00"
    }
]
# Group transactions using a dictionary
groups = {}
for transaction in transactions:
    key = (
        transaction["account"],
        transaction["amount"],
        transaction["merchant"]
    )
    if key not in groups:
        groups[key] = []
    groups[key].append(transaction)
# Find duplicate transactions within 60 seconds
duplicate_pairs = []
for key, group in groups.items():
    # Sort each group by timestamp
    group.sort(
        key=lambda x: datetime.strptime(
            x["timestamp"], "%Y-%m-%d %H:%M:%S"
        )
    )
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            time1 = datetime.strptime(
                group[i]["timestamp"], "%Y-%m-%d %H:%M:%S"
            )
            time2 = datetime.strptime(
                group[j]["timestamp"], "%Y-%m-%d %H:%M:%S"
            )
            difference = (time2 - time1).total_seconds()
            if difference <= 60:
                duplicate_pairs.append((group[i], group[j]))
            else:
                # Later transactions will be even farther away
                break
# Display results
print("Total Transactions Checked:", len(transactions))
print("Duplicate Pairs Found:", len(duplicate_pairs))
print("\n--- Duplicate Posting Details ---")
for first, second in duplicate_pairs:
    print("\nAccount:", first["account"])
    print("Amount:", first["amount"])
    print("Merchant:", first["merchant"])
    print("Transaction 1:", first["transactionId"])
    print("Transaction 2:", second["transactionId"])
    print("Time Difference: 60 seconds or less")
