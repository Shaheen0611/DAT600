
# Map index to labels
labels = ['A', 'B', 'C', 'D', 'E', 'F']

def adjacency_matrix_to_list(matrix):
    adj_list = {}
    for i, row in enumerate(matrix):
        neighbors = [labels[j] for j, val in enumerate(row) if val == 1]
        adj_list[labels[i]] = sorted(neighbors)  # Ensure alphabetical order
    return adj_list

# Generate adjacency list
Adj = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
]

adj_list = adjacency_matrix_to_list(Adj)
for node in sorted(adj_list):
    print(f"{node}: {adj_list[node]}")

