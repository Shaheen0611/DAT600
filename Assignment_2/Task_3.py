def greedy_coin_change(coins, N):
    """Greedy algorithm to minimize the number of coins required for total N."""
    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    result = []
    
    for coin in coins:
        while N >= coin:
            N -= coin
            count += 1
            result.append(coin)
    
    return count, result

def dp_coin_change(coins, N):
    """Dynamic programming solution for the minimum number of coins required."""
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for amount in range(1, N + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[N] if dp[N] != float('inf') else -1

def is_greedy_optimal(coins):
    """Check if a given coin system is greedy-optimal (follows the greedy choice property)."""
    for i in range(1, sum(coins)):
        if greedy_coin_change(coins, i)[0] != dp_coin_change(coins, i):
            return False
    return True

# Example Usage
coins = [1, 5, 10, 20]  # Norwegian coin system
N = 15

print("Greedy Solution:", greedy_coin_change(coins, N))
print("DP Solution:", dp_coin_change(coins, N))
print("Is Norwegian coin system greedy-optimal?", is_greedy_optimal(coins))
