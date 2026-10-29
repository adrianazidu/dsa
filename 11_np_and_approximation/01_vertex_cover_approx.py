"""
ALGORITHM: NP-Completeness & 2-Approximation for Vertex Cover

WHAT IT DOES (SIMPLY):
Imagine a museum where hallways connect different galleries. You want to place security guards
at hallway junctions so that every single hallway is watched by at least one guard, using the
absolute minimum number of guards. This problem is "NP-Complete" (finding the exact minimum
number would take a computer millions of years for huge buildings). Instead, this approximation
algorithm finishes in milliseconds and guarantees it will use at most TWICE the minimum possible guards.

REAL-LIFE USE CASES:
- Network Security Monitoring: Placing network monitors at server switches to inspect all data traffic.
- Road Traffic Camera Placement: Placing traffic cameras at intersections to cover all major streets.
- Bio-Informatics & Genetic Testing: Selecting the smallest set of proteins or genes that interact with all targets.
"""

# Exact polynomial-time verifier for a Vertex Cover certificate
def verify_vertex_cover(edges, candidate_nodes):
    cover_set = set(candidate_nodes)
    for u, v in edges:
        if u not in cover_set and v not in cover_set:
            return False
    return True


# 2-Approximation Algorithm for Minimum Vertex Cover
def approx_vertex_cover(edges):
    cover = set()
    uncovered = list(edges)

    while uncovered:
        # Greedily pick arbitrary remaining uncovered edge
        u, v = uncovered.pop()

        if u not in cover and v not in cover:
            # Include BOTH endpoints in the cover
            cover.add(u)
            cover.add(v)
            # Remove any edge that has now been covered by u or v
            uncovered = [
                (x, y)
                for x, y in uncovered
                if x != u and x != v and y != u and y != v
            ]

    return cover


if __name__ == "__main__":
    graph_edges = [(0, 1), (1, 2), (2, 3), (3, 0), (1, 3)]
    approx = approx_vertex_cover(graph_edges)
    print(f"Approximate Vertex Cover: {approx}")
    print(f"Valid Cover Check: {verify_vertex_cover(graph_edges, approx)}")
