import heapq

# --- Dijkstra's Algorithm ---
def dijkstra(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

# --- Bellman-Ford Algorithm (for 4b) ---
def bellman_ford(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    # Check for negative cycles
    for u in graph:
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                raise ValueError("Graph contains a negative weight cycle")

    return dist

# --- Graph Definition (A → B → C, with negative edge) ---
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', -3)],
    'C': []
}

# --- Run Dijkstra ---
dijkstra_result = dijkstra(graph, 'A')

# --- Run Bellman-Ford ---
bellman_result = bellman_ford(graph, 'A')

# --- Display Results ---
print("=== Problem 4a: Dijkstra Result (Incorrect with Negative Edge) ===")
for node in sorted(graph):
    print(f"A -> {node} = {dijkstra_result[node]}")

print("\n=== Problem 4b: Bellman-Ford Result (Correct for Negative Edge) ===")
for node in sorted(graph):
    print(f"A -> {node} = {bellman_result[node]}")
