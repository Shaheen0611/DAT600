from collections import defaultdict, deque

# ------------------------------
# BFS for Reachability (Champions)
# ------------------------------
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return visited

def find_champions(graph):
    champions = []
    all_nodes = set(graph.keys())
    for node in graph:
        reachable = bfs(graph, node)
        if reachable == all_nodes:
            champions.append(node)
    return champions

# ------------------------------
# Kosaraju's Algorithm for SCCs
# ------------------------------
def dfs_finish_times(graph, node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_finish_times(graph, neighbor, visited, stack)
    stack.append(node)

def reverse_graph(graph):
    reversed_g = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            reversed_g[v].append(u)
    return reversed_g

def dfs_collect_scc(graph, node, visited, current_scc):
    visited.add(node)
    current_scc.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_collect_scc(graph, neighbor, visited, current_scc)

def kosaraju_scc(graph):
    visited = set()
    stack = []

    # 1. DFS to compute finish times
    for node in graph:
        if node not in visited:
            dfs_finish_times(graph, node, visited, stack)

    # 2. Reverse the graph
    reversed_g = reverse_graph(graph)

    # 3. DFS in finish time order on reversed graph
    visited.clear()
    sccs = []

    while stack:
        node = stack.pop()
        if node not in visited:
            current_scc = []
            dfs_collect_scc(reversed_g, node, visited, current_scc)
            sccs.append(sorted(current_scc))

    return sccs

# ------------------------------
# Example Graph (From Assignment Figure 3)
# ------------------------------
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['C', 'D'],
    'C': [],
    'D': ['B', 'C'],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

# Ensure all nodes are present even if they have no outgoing edges
for u in list(graph.keys()):
    for v in graph[u]:
        if v not in graph:
            graph[v] = []

# ------------------------------
# Output: Champions (3a)
# ------------------------------
print("=== Champions in the Tournament (3a) ===")
champions = find_champions(graph)
if champions:
    for c in champions:
        print(f"{c}")
else:
    print("No champions found.")

# ------------------------------
# Output: SCC Groups (3b)
# ------------------------------
print("\n=== Strongly Connected Groups (3b) ===")
scc_groups = kosaraju_scc(graph)
for idx, group in enumerate(scc_groups, 1):
    print(f"Group {idx}: {{ {', '.join(group)} }}")
