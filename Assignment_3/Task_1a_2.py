import networkx as nx
import matplotlib.pyplot as plt


Adj = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
]

G = nx.DiGraph()
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

# Add edges from the matrix
for i in range(len(Adj)):
    for j in range(len(Adj[i])):
        if Adj[i][j] == 1:
            G.add_edge(nodes[i], nodes[j])




# Draw the graph
plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True)
plt.title("Graph from Adjacency Matrix")
plt.show()
