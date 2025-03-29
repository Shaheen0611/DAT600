# Step 1: Graph from Figure 1
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
    'J': ['F']  # This causes a cycle
}

# Step 2: Remove one edge to break the cycle (e.g. remove J → F)
if 'F' in graph['J']:
    graph['J'].remove('F')

# Step 3: Topological Sort using DFS
visited = set()
stack = []

def topo_sort(node):
    visited.add(node)
    for neighbor in sorted(graph.get(node, [])):  # alphabetical order
        if neighbor not in visited:
            topo_sort(neighbor)
    stack.append(node)

# Perform topological sort for all nodes
for node in sorted(graph.keys()):
    if node not in visited:
        topo_sort(node)

# Step 4: Output result
print("=== Topological Sort Order (after removing J → F) ===")
print(" -> ".join(stack[::-1]))  # reverse the stack
