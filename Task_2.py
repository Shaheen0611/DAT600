import random

def generate_knapsack_problem(n, max_weight, max_value):
    """Generates a list of items with random weights and values."""
    items = [(random.randint(1, max_weight), random.randint(1, max_value)) for _ in range(n)]
    return items

def knapsack_01(items, capacity):
    """Solves the 0-1 knapsack problem using dynamic programming."""
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

def fractional_knapsack(items, capacity):
    """Solves the fractional knapsack problem using a greedy approach."""
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    
    for weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += (value / weight) * capacity
            break
    
    return total_value

# Example Usage
n = 5  # Number of items
max_weight = 10
max_value = 50
capacity = 20

items = generate_knapsack_problem(n, max_weight, max_value)
print("Generated items (weight, value):", items)
print("0-1 Knapsack Solution:", knapsack_01(items, capacity))
print("Fractional Knapsack Solution:", fractional_knapsack(items, capacity))