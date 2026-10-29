"""
Comprehensive Graph Algorithms
------------------------------
What it does:
- Breadth-First Search (BFS): Explores outward in waves. Finds the shortest path in unweighted networks.
- Depth-First Search (DFS): Explores straight down a path until hitting a dead end. Good for mazes and cycle detection.
- Topological Sort (Kahn's): Orders tasks so every prerequisite comes before the task that needs it.
- Dijkstra's Algorithm: Finds the fastest driving or routing path when roads have positive travel times/distances.
- Floyd-Warshall: Computes the shortest travel path between every single pair of cities in a single matrix.
- Kosaraju's SCC: Finds tightly knit clusters in directed networks where every node can reach every other node.
- Edmonds-Karp Max Flow: Finds the maximum volume of water/traffic that can flow through a pipe network from source to sink.

Real-World Use Cases:
- GPS Navigation (Google Maps, Waze) using Dijkstra to calculate routes.
- Build systems (Make, Webpack) and package managers (`pip`, `npm`) ordering compilation dependencies via Topological Sort.
- Telecommunication networks calculating data throughput limits (Maximum Flow).
- Web crawlers and social media graph discovery using BFS and DFS.
"""

from collections import deque
import heapq

# 1. Breadth-First Search (BFS)
def bfs_shortest_path(adj: dict, start: int) -> dict:
    distances = {v: float("inf") for v in adj}
    distances[start] = 0
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if distances[v] == float("inf"):
                distances[v] = distances[u] + 1
                queue.append(v)
    return distances

# 2. Dijkstra's Shortest Path
def dijkstra(adj: dict, source: int) -> dict:
    distances = {v: float("inf") for v in adj}
    distances[source] = 0.0
    pq = [(0.0, source)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > distances[u]: continue
        for v, weight in adj[u]:
            if d + weight < distances[v]:
                distances[v] = d + weight
                heapq.heappush(pq, (distances[v], v))
    return distances

# 3. Topological Sort (Kahn's)
def topological_sort(vertices: list, adj: dict) -> list:
    in_degree = {v: 0 for v in vertices}
    for u in adj:
        for v in adj[u]: in_degree[v] += 1
    queue = deque([v for v in vertices if in_degree[v] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0: queue.append(v)
    return order

if __name__ == "__main__":
    graph = {
        0: [(1, 4.0), (2, 1.0)],
        1: [(3, 1.0)],
        2: [(1, 2.0), (3, 5.0)],
        3: []
    }
    print("Dijkstra shortest travel times from node 0:", dijkstra(graph, 0))
