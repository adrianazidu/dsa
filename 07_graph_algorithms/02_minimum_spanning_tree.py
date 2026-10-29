"""
ALGORITHM: Minimum Spanning Tree (Kruskal's Algorithm)

WHAT IT DOES (SIMPLY):
Imagine you need to lay cables between a group of houses. You want to make sure
every single house is connected to every other house (either directly or via another house),
but you want to buy the minimum total length of cable possible and avoid creating useless
loops. Kruskal's algorithm solves this by repeatedly picking the cheapest available connection
that doesn't form a closed loop until everyone is connected.

REAL-LIFE USE CASES:
- Telecom & Cable Laying: Designing fiber-optic networks connecting neighborhoods at minimum cost.
- Utility Grids: Laying electrical power grids and clean water piping across cities.
- Circuit Board (VLSI) Design: Connecting pins on a microchip using minimal wire length and capacitance.
- Machine Learning: Single-linkage hierarchical clustering (detecting natural groupings of data).
"""

# Define the Disjoint Set Union (DSU) class to manage connected components
class DisjointSet:
    # Initialize the structure for 'n' elements (0 to n - 1)
    def __init__(self, n):
        # Each element initially points to itself as its own parent
        self.parent = [i for i in range(n)]
        # Track tree depth (rank) to keep the trees flat during unions
        self.rank = [0] * n

    # Find the representative root of the set containing element 'i'
    def find(self, i):
        # If 'i' is not its own parent, recursively find the root
        if self.parent[i] != i:
            # Path compression: point node directly to root
            self.parent[i] = self.find(self.parent[i])
        # Return the root representative
        return self.parent[i]

    # Merge the sets containing elements 'u' and 'v'
    def union(self, u, v):
        # Locate the root of node 'u'
        root_u = self.find(u)
        # Locate the root of node 'v'
        root_v = self.find(v)

        # If both nodes share the same root, they are already connected (cycle)
        if root_u == root_v:
            return False

        # Union by rank: attach shorter tree under taller tree
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


# Function to compute Minimum Spanning Tree using Kruskal's algorithm
def kruskal_mst(num_vertices, edges):
    # Sort all edges in non-decreasing order of weight: (u, v, weight)
    edges.sort(key=lambda edge: edge[2])
    # Instantiate DSU structure
    dsu = DisjointSet(num_vertices)
    # Output list of chosen MST edges
    mst_edges = []
    # Total accumulated edge weight
    total_cost = 0

    # Iterate through sorted edges
    for u, v, weight in edges:
        # Union endpoints; True if in different sets
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_cost += weight
            # Early stop when exactly V - 1 edges are selected
            if len(mst_edges) == num_vertices - 1:
                break

    return mst_edges, total_cost


if __name__ == "__main__":
    v_count = 4
    sample_edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    chosen, cost = kruskal_mst(v_count, sample_edges)
    print(f"MST Edges: {chosen}")
    print(f"Total Cost: {cost}")
