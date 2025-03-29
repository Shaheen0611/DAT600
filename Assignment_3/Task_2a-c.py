# Shared: Union-Find and Kruskal

class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

def kruskal_mst(edges, vertices):
    uf = UnionFind(vertices)
    mst = []
    total_cost = 0
    for cost, u, v in sorted(edges):
        if uf.union(u, v):
            mst.append((u, v, cost))
            total_cost += cost
    return mst, total_cost

# ============================
# Problem 2a: Basic MST within budget
# ============================

def problem_2a():
    edges = [
        (1, 'A', 'B'),
        (5, 'A', 'C'),
        (4, 'B', 'D'),
        (8, 'C', 'D'),
        (2, 'C', 'E'),
        (4, 'D', 'F'),
        (2, 'E', 'F'),
        (6, 'E', 'G'),
        (9, 'F', 'H'),
        (7, 'G', 'H')
    ]
    vertices = list(set([u for _, u, v in edges] + [v for _, u, v in edges]))
    budget = 30
    mst, total = kruskal_mst(edges, vertices)

    print("=== Problem 2a: MST within Budget ===")
    for u, v, cost in mst:
        print(f"{u} -- {v} : {cost}")
    print(f"Total MST Cost: {total}")
    print(f"Within Budget ({budget})? {'Yes' if total <= budget else 'No'}\n")


# ============================
# Problem 2b: Max 3 edges for D
# ============================

def kruskal_with_degree_limit(edges, vertices, degree_limit_node, max_degree):
    uf = UnionFind(vertices)
    mst = []
    total_cost = 0
    degree_count = {v: 0 for v in vertices}

    for cost, u, v in sorted(edges):
        if (u == degree_limit_node and degree_count[u] >= max_degree) or \
           (v == degree_limit_node and degree_count[v] >= max_degree):
            continue

        if uf.union(u, v):
            mst.append((u, v, cost))
            total_cost += cost
            degree_count[u] += 1
            degree_count[v] += 1

    connected_components = set(uf.find(v) for v in vertices)
    all_connected = len(connected_components) == 1
    return mst, total_cost, degree_count, all_connected

def problem_2b():
    edges = [
        (1, 'A', 'B'),
        (5, 'A', 'C'),
        (4, 'B', 'D'),
        (8, 'C', 'D'),
        (2, 'C', 'E'),
        (4, 'D', 'F'),
        (2, 'E', 'F'),
        (6, 'E', 'G'),
        (9, 'F', 'H'),
        (7, 'G', 'H')
    ]
    vertices = list(set([u for _, u, v in edges] + [v for _, u, v in edges]))
    budget = 30
    max_d_edges = 3

    mst, total, degrees, connected = kruskal_with_degree_limit(
        edges, vertices, 'D', max_d_edges
    )

    print("=== Problem 2b: MST with D ≤ 3 Edges ===")
    for u, v, cost in mst:
        print(f"{u} -- {v} : {cost}")
    print(f"Total Cost: {total}")
    print(f"D has {degrees['D']} edges (limit: {max_d_edges})")
    print(f"All nodes connected? {'Yes' if connected else 'No'}")
    print(f"Within Budget ({budget})? {'Yes' if total <= budget else 'No'}\n")


# ============================
# Problem 2c: Modified Edge Swap to meet b' = 25
# ============================

def problem_2c():
    original_edges = [
        (1, 'A', 'B'),
        (5, 'A', 'C'),
        (4, 'B', 'D'),
        (8, 'C', 'D'),
        (2, 'C', 'E'),
        (4, 'D', 'F'),
        (2, 'E', 'F'),
        (6, 'E', 'G'),
        (9, 'F', 'H'),
        (7, 'G', 'H')
    ]

    # Modify: change (A, B) to 6, and add (C, G) = 5
    modified_edges = []
    for cost, u, v in original_edges:
        if (u, v) == ('A', 'B') or (v, u) == ('A', 'B'):
            modified_edges.append((6, u, v))  # increase A-B
        else:
            modified_edges.append((cost, u, v))
    modified_edges.append((5, 'C', 'G'))

    vertices = list(set([u for _, u, v in modified_edges] + [v for _, u, v in modified_edges]))
    budget_prime = 25

    mst, total = kruskal_mst(modified_edges, vertices)

    print("=== Problem 2c: MST After Edge Swap ===")
    for u, v, cost in mst:
        print(f"{u} -- {v} : {cost}")
    print(f"Total MST Cost: {total}")
    print(f"Within Modified Budget (b' = {budget_prime})? {'Yes' if total <= budget_prime else 'No'}\n")

if __name__ == "__main__":
    problem_2a()
    problem_2b()
    problem_2c()
