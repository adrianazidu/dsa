"""
ALGORITHM: Metric Traveling Salesperson Problem (Metric TSP 2-Approximation)

WHAT IT DOES (SIMPLY):
A delivery driver needs to visit 50 cities and return home, driving the shortest total
distance possible. Finding the absolute best route is mathematically intractable (NP-Hard).
However, in the real world, detours are always longer than driving direct (the "triangle inequality").
This algorithm builds a cheap backbone tree connecting all cities and shortcuts directly
between stops, guaranteeing the total trip is never more than TWICE the perfect route.

REAL-LIFE USE CASES:
- Package Delivery & Logistics: Amazon, UPS, and DHL calculating multi-stop daily delivery truck routes.
- Semiconductor Manufacturing: Programming robotic drilling arms to drill thousands of micro-holes on circuit boards.
- School Bus & Garbage Collection: Routing public service vehicles through neighborhoods with minimal fuel.
"""

from collections import defaultdict


# Euclidean distance satisfying triangle inequality
def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


# Prim's algorithm for coordinate MST
def build_mst(points):
    n = len(points)
    in_tree = [False] * n
    min_cost = [float("inf")] * n
    parent = [-1] * n
    min_cost[0] = 0

    for _ in range(n):
        u = min(
            (c, i)
            for i, (c, visited) in enumerate(zip(min_cost, in_tree))
            if not visited
        )[1]
        in_tree[u] = True

        for v in range(n):
            if not in_tree[v]:
                d = dist(points[u], points[v])
                if d < min_cost[v]:
                    min_cost[v] = d
                    parent[v] = u

    adj = defaultdict(list)
    for v in range(1, n):
        adj[parent[v]].append(v)
        adj[v].append(parent[v])
    return adj


# 2-Approximation for Metric TSP via MST Double-Tree Traversal
def metric_tsp_approx(points):
    mst_adj = build_mst(points)
    visited = [False] * len(points)
    tour = []

    # Preorder walk shortcuts past visited nodes
    def dfs(u):
        visited[u] = True
        tour.append(u)
        for neighbor in mst_adj[u]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(0)
    tour.append(tour[0])

    total_len = sum(
        dist(points[tour[i]], points[tour[i + 1]])
        for i in range(len(tour) - 1)
    )
    return tour, total_len


if __name__ == "__main__":
    coords = [(0, 0), (1, 5), (5, 6), (6, 1), (3, 3)]
    order, length = metric_tsp_approx(coords)
    print(f"Tour Path: {order}")
    print(f"Tour Length: {length:.3f}")
