# Define the graph based on Figure 1
# Each node's edges are listed and sorted alphabetically

def get_figure1_adjacency_list():
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

    # Sort the adjacency lists alphabetically
    for node in graph:
        graph[node] = sorted(graph[node])

    return graph

# Use the function and print the list
adj_list = get_figure1_adjacency_list()
for node in sorted(adj_list.keys()):
    print(f"{node}: {adj_list[node]}")
