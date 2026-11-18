# Greedy Algorithm for Refund
def greedy_refund(amount, denominations):
    result = []
    for coin in denominations:
        count = amount // coin
        if count > 0:
            result.append((coin, count))
            amount = amount % coin
    return result
# Test with standard denominations
denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
amount = 786
refund = greedy_refund(amount, denominations)
print("Refund Amount:", amount)
print("Greedy Refund:", refund)
print("Total Notes/Coins:", sum(count for coin, count in refund))
# Example where Greedy fails
denominations = [4, 3, 1]
amount = 6
greedy_result = greedy_refund(amount, denominations)
print("\n--- Greedy Failure Example ---")
print("Refund Amount:", amount)
print("Greedy Refund:", greedy_result)
print("Total Notes/Coins:",
      sum(count for coin, count in greedy_result))
# Dynamic Programming for Minimum Refund
def dp_refund(amount, denominations):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in denominations:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]
# Compare Greedy and Dynamic Programming
denominations = [4, 3, 1]
amount = 6
optimal_count = dp_refund(amount, denominations)
print("\n--- Dynamic Programming Result ---")
print("Refund Amount:", amount)
print("Minimum Notes/Coins:", optimal_count)