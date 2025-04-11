import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges with capacities based on the provided network
edges = [
    ("s", "v1", 14),
    ("s", "v2", 25),
    ("v1", "v3", 6),
    ("v1", "v4", 21),
    ("v2", "v3", 13),
    ("v2", "v5", 7),
    ("v3", "v1", 3),
    ("v3", "v4", 10),
    ("v3", "v5", 15),
    ("v4", "t", 20),
    ("v5", "v4", 5),
    ("v5", "t", 10),
]

# Add edges to the graph with capacity attributes
for u, v, cap in edges:
    G.add_edge(u, v, capacity=cap)

# Solve the minimum cut problem
cut_value, (reachable, non_reachable) = nx.minimum_cut(G, "s", "t")

# Print the result
print("=== Task 2a: Minimum Cut ===")
print(f"Minimum cut value (capacity): {cut_value}")
print(f"Source side of cut (reachable): {reachable}")
print(f"Sink side of cut (non-reachable): {non_reachable}")

# Print edges that form the cut
cut_edges = [
    (u, v)
    for u in reachable
    for v in G[u]
    if v in non_reachable
]
print("Cut edges (bottlenecks):", cut_edges)

# Solve the maximum flow problem using the same graph G
flow_value, flow_dict = nx.maximum_flow(G, "s", "t")

# Print the result
print("\n=== Task 2b: Maximum Flow ===")
print(f"Maximum flow from s to t: {flow_value}")
print("Flow per edge:")

# Print the flow dictionary in a readable format
for u in flow_dict:
    for v in flow_dict[u]:
        flow = flow_dict[u][v]
        if flow > 0:
            print(f"{u} → {v}: {flow}")
