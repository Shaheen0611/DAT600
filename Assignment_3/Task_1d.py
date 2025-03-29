# Original graph with cycles from Figure 1
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
    'J': ['F']  # ← this edge creates a cycle
}

# Make sure neighbor lists are sorted
for node in graph:
    graph[node] = sorted(graph[node])

# --- Function to remove back edges (i.e., convert to DAG) ---
def remove_cycles(graph):
    visited = set()
    recursion_stack = set()
    edges_to_remove = []

    def dfs(node):
        visited.add(node)
        recursion_stack.add(node)

        for neighbor in list(graph.get(node, [])):  # use list to avoid modifying during iteration
            if neighbor not in visited:
                dfs(neighbor)
            elif neighbor in recursion_stack:
                # Found a cycle! Mark edge for removal
                edges_to_remove.append((node, neighbor))
                graph[node].remove(neighbor)  # remove the back edge immediately

        recursion_stack.remove(node)

    # Run DFS on all nodes
    for node in sorted(graph):
        if node not in visited:
            dfs(node)

    return edges_to_remove

# --- Run the DAG converter ---
removed_edges = remove_cycles(graph)

# --- Print results ---
print("=== Edges Removed to Make DAG ===")
for u, v in removed_edges:
    print(f"{u} -> {v}")

print("\n=== DAG (Adjacency List After Cycle Removal) ===")
for node in sorted(graph):
    print(f"{node}: {graph[node]}")
