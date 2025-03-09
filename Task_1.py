import numpy as np

def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = np.zeros((n, n))  # Table to store minimum scalar multiplications
    s = np.zeros((n, n), dtype=int)  # Table to store split points
    
    for chain_length in range(2, n + 1):  # Length of matrix chain
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            m[i, j] = float('inf')
            for k in range(i, j):
                cost = m[i, k] + m[k+1, j] + p[i] * p[k+1] * p[j+1]
                if cost < m[i, j]:
                    m[i, j] = cost
                    s[i, j] = k
    return m, s

def print_optimal_parenthesization(s, i, j):
    if i == j:
        return f"A{i+1}"
    else:
        return f"({print_optimal_parenthesization(s, i, s[i, j])} * {print_optimal_parenthesization(s, s[i, j] + 1, j)})"

# Example usage
dimensions = [10, 30, 5, 60, 20, 50]
m, s = matrix_chain_order(dimensions)
optimal_parenthesization = print_optimal_parenthesization(s, 0, len(dimensions) - 2)
print("Optimal Parenthesization:", optimal_parenthesization)
print("Minimum Cost:", m[0, len(dimensions) - 2])