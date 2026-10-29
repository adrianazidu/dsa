"""
ALGORITHM: Maximum Flow (Edmonds-Karp / Ford-Fulkerson Algorithm)

WHAT IT DOES (SIMPLY):
Imagine a network of water pipes of varying diameters connecting a water reservoir (source)
to a town (sink). You want to know the maximum amount of water you can pump through the system
per minute without bursting any single pipe. This algorithm repeatedly finds paths with room to spare
and sends flow through them until the system hits its overall bottleneck.

REAL-LIFE USE CASES:
- Pipeline & Power Grids: Measuring maximum oil/gas throughput or electricity transmission limits.
- Bipartite Job Assignment: Pairing interns to jobs or doctors to hospital shifts based on availability and skills.
- CDN & Video Streaming: Routing live video streams across congested internet backbones without buffering.
- Airline Scheduling: Matching flight crews and aircraft to flight legs across daily schedules.
"""

# Import deque for FIFO queue BFS traversal
from collections import deque


# Edmonds-Karp algorithm for maximum flow
def edmonds_karp(capacity, source, sink, num_vertices):
    # Initialize residual capacity matrix as duplicate of capacity
    residual = [row[:] for row in capacity]
    max_flow = 0

    # Helper BFS function to find augmenting paths in the residual graph
    def bfs(parent_tracker):
        visited = [False] * num_vertices
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()
            for v in range(num_vertices):
                # Traverse unvisited edges with remaining capacity
                if not visited[v] and residual[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent_tracker[v] = u
                    if v == sink:
                        return True
        return False

    parent = [-1] * num_vertices

    # Augment paths until no path from source to sink remains
    while bfs(parent):
        path_flow = float("inf")
        curr = sink

        # Find bottleneck capacity along discovered augmenting path
        while curr != source:
            prev = parent[curr]
            path_flow = min(path_flow, residual[prev][curr])
            curr = prev

        # Update residual capacities on forward and reverse edges
        curr = sink
        while curr != source:
            prev = parent[curr]
            residual[prev][curr] -= path_flow
            residual[curr][prev] += path_flow
            curr = prev

        max_flow += path_flow

    return max_flow


if __name__ == "__main__":
    n = 6
    cap = [[0] * n for _ in range(n)]
    edges = [
        (0, 1, 16),
        (0, 2, 13),
        (1, 2, 10),
        (1, 3, 12),
        (2, 1, 4),
        (2, 4, 14),
        (3, 2, 9),
        (3, 5, 20),
        (4, 3, 7),
        (4, 5, 4),
    ]
    for u, v, c in edges:
        cap[u][v] = c

    flow = edmonds_karp(cap, source=0, sink=5, num_vertices=n)
    print(f"Max Flow: {flow}")
