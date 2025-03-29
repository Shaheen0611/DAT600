from collections import defaultdict, deque


def print_problem_5a_answer():
    explanation = """
=== Problem 5a: Resolving Antiparallel Edges in a Flow Network ===

Antiparallel edges occur when there are two directed edges between the same two nodes 
in opposite directions, such as (u → v) and (v → u).

In flow networks, antiparallel edges are resolved by using a residual graph.
This means that for every edge (u → v), we automatically maintain a reverse edge (v → u) 
in the residual graph. The reverse edge allows the algorithm to 'undo' flow, making it 
possible to find augmenting paths even when backtracking is needed.

This method allows modern flow algorithms like Ford-Fulkerson and Edmonds-Karp to handle 
antiparallel edges naturally, without requiring changes to the graph structure.

✅ Conclusion:
Antiparallel edges do not need to be removed or split manually. They are correctly 
handled by maintaining residual capacities and reverse edges in the algorithm's residual graph.
"""

    print(explanation)

# Run the function
print_problem_5a_answer()


class MaxFlow:
    
    def __init__(self, graph):
        self.graph = defaultdict(dict)
        self.build_graph(graph)

    def build_graph(self, edge_list):
        for u, v, capacity in edge_list:
            self.graph[u][v] = capacity
            if v not in self.graph or u not in self.graph[v]:
                self.graph[v][u] = 0  # reverse edge in residual graph

    def bfs(self, s, t, parent):
        visited = set()
        queue = deque([s])
        visited.add(s)
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if v not in visited and self.graph[u][v] > 0:
                    parent[v] = u
                    visited.add(v)
                    queue.append(v)
                    if v == t:
                        return True
        return False

    def ford_fulkerson(self, s, t):
        parent = {}
        max_flow = 0

        while self.bfs(s, t, parent):
            # Find bottleneck (min capacity in path)
            path_flow = float('inf')
            v = t
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = u

            # Update residual capacities
            v = t
            while v != s:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

            max_flow += path_flow
            parent = {}  # Reset for next iteration

        return max_flow

    def min_cut(self, s):
        visited = set()
        queue = deque([s])
        visited.add(s)

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if self.graph[u][v] > 0 and v not in visited:
                    visited.add(v)
                    queue.append(v)
        return visited  # This is the source side of the min cut


# --- Graph from Assignment (Figure 5) ---
edges = [
    ('s', 'V1', 14),
    ('s', 'V2', 10),
    ('V1', 'V2', 3),
    ('V1', 'V3', 2),
    ('V2', 'V4', 25),
    ('V3', 'V5', 20),
    ('V4', 'V3', 15),
    ('V4', 'V5', 10),
    ('V5', 't', 5),
    ('V4', 't', 10)
]

# --- Run Ford-Fulkerson ---
mf = MaxFlow(edges)
maxflow = mf.ford_fulkerson('s', 't')

print("=== Problem 5b: Maximum Flow ===")
print(f"Max flow from s to t: {maxflow}")

# --- Problem 5c: Show the bottleneck via cuts ---
mincut_set = mf.min_cut('s')
print("\n=== Problem 5c: Bottleneck (Min Cut) ===")
print(f"Source side of Min Cut: {mincut_set}")
print(f"Sink side of Min Cut: {set(mf.graph.keys()) - mincut_set}")

# --- Problem 5d: Runtime & Improvement ---
print("\n=== Problem 5d: Runtime & Improvement ===")
print("Ford-Fulkerson Runtime: O(E * max_flow)")
print("Improvement: Use Edmonds-Karp (BFS-based) → Runtime: O(V * E^2)")
