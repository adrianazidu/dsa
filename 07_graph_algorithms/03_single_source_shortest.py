"""
ALGORITHM: Single-Source Shortest Path (Dijkstra's Algorithm)

WHAT IT DOES (SIMPLY):
Imagine you are at home and want to know the quickest driving route to every other
location in town. Unlike a spanning tree (which cares about the total network cost),
Dijkstra's algorithm focuses purely on the fastest trip from your single starting point
to all other destinations. It works by always exploring the closest unexplored intersection next.

REAL-LIFE USE CASES:
- GPS Turn-by-Turn Navigation: Google Maps, Waze, and Apple Maps computing the quickest driving route.
- Internet Data Routing (OSPF Protocol): Routers choosing the lowest-latency path to forward packets.
- Logistics Dispatch: Finding the quickest travel times from a central distribution hub to customer drop-offs.
"""

# Import heapq module for min-heap priority queue operations
import heapq


# Dijkstra's Single-Source Shortest Path algorithm
def dijkstra(graph, source):
    # Initialize all distances to positive infinity
    distances = {node: float("inf") for node in graph}
    # Distance from source to itself is zero
    distances[source] = 0
    # Map to track predecessors for path reconstruction
    predecessors = {node: None for node in graph}
    # Priority queue stores tuples of (distance, node_id)
    pq = [(0, source)]

    # Loop until all reachable nodes have been processed
    while pq:
        # Pop unvisited node with smallest tentative distance
        current_dist, current_node = heapq.heappop(pq)

        # Stale entry check: skip if better path was already recorded
        if current_dist > distances[current_node]:
            continue

        # Inspect each neighbor of the current node
        for neighbor, weight in graph[current_node]:
            # Calculate distance to neighbor via current node
            new_dist = current_dist + weight
            # Relaxation step: update if new path is shorter
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (new_dist, neighbor))

    return distances, predecessors


if __name__ == "__main__":
    adj_graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2)],
        "E": [("C", 10), ("D", 2)],
    }
    dists, preds = dijkstra(adj_graph, "A")
    print(f"Shortest distances from A: {dists}")
