"""
ALGORITHM: All-Pairs Shortest Path (Floyd-Warshall Algorithm)

WHAT IT DOES (SIMPLY):
Instead of finding the shortest path from just one starting point, this algorithm
calculates the shortest distance between EVERY possible pair of locations in the network.
It does this by testing whether taking a detour through any intermediate stop 'k' makes the
trip between city 'i' and city 'j' shorter than the current direct path.

REAL-LIFE USE CASES:
- Flight Booking Engines: Generating tables of the cheapest/quickest connecting flights between all world airports.
- Social Network Analysis: Calculating degrees of separation and "centrality" (who is closest to everyone on LinkedIn/X).
- Urban Transit Planning: Computing complete travel-time matrices between all metro stations and neighborhoods.
"""

# Floyd-Warshall All-Pairs Shortest Path algorithm
def floyd_warshall(num_vertices, edges):
    # Initialize V x V distance matrix filled with infinity
    dist = [[float("inf")] * num_vertices for _ in range(num_vertices)]

    # Distance from any node to itself is zero
    for i in range(num_vertices):
        dist[i][i] = 0

    # Fill direct edge weights: (u, v, weight)
    for u, v, weight in edges:
        dist[u][v] = weight

    # Intermediate pivot node loop
    for k in range(num_vertices):
        # Starting node loop
        for i in range(num_vertices):
            # Destination node loop
            for j in range(num_vertices):
                # Check reachability of intermediate path
                if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    # Relaxation step
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    # Verify absence of negative weight cycles
    for i in range(num_vertices):
        if dist[i][i] < 0:
            raise ValueError("Graph contains a negative weight cycle")

    return dist


if __name__ == "__main__":
    nodes = 4
    edge_defs = [(0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1), (3, 0, 2)]
    matrix = floyd_warshall(nodes, edge_defs)
    print("All-Pairs Distance Matrix:")
    for row in matrix:
        print(row)
