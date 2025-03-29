from collections import defaultdict, deque

# --- Define the graph from Figure 1 (adjacency list, sorted alphabetically) ---
graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['B', 'E'],
    'D': ['B', 'F'],
    'E': ['F', 'G', 'J'],
    'F': ['B', 'H'],
    'G': ['I'],
    'H': ['J'],
    'I': ['J'],
    'J': ['F']
}

# Sort neighbors alphabetically
for node in graph:
    graph[node] = sorted(graph[node])


# === BFS Implementation ===
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Enqueue neighbors not yet visited
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return order


# === DFS Implementation with Discovery and Finish Times ===
def dfs_with_timestamps(graph, start):
    time = 0
    discovery = {}
    finish = {}
    visited = set()
    dfs_order = []

    def dfs(node):
        nonlocal time
        visited.add(node)
        time += 1
        discovery[node] = time
        dfs_order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

        time += 1
        finish[node] = time

    dfs(start)
    return dfs_order, discovery, finish


# --- Run both traversals ---
bfs_order = bfs(graph, 'A')
dfs_order, discovery, finish = dfs_with_timestamps(graph, 'A')

# --- Print BFS Result ---
print("=== BFS Order ===")
print(" -> ".join(bfs_order))

# --- Print DFS Result ---
print("\n=== DFS Order ===")
print(" -> ".join(dfs_order))

print("\n=== Discovery and Finish Times ===")
for node in dfs_order:
    print(f"{node}: d = {discovery[node]}, f = {finish[node]}")
