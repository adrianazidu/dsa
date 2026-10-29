"""
Disjoint-Set Union (Union-Find)
-------------------------------
What it does:
Tracks a collection of elements split into non-overlapping groups.
- `find(x)`: Identifies which group an item belongs to.
- `union(x, y)`: Merges two groups together.
Uses two clever tricks ("Path Compression" and "Union by Rank") to make lookups and merges operate in practically instantaneous time.

Real-World Use Cases:
- Kruskal's algorithm for building Minimum Spanning Trees (ensures new connections don't create cycles).
- Social network analysis: quickly checking if two users are connected in the same friend community.
- Computer vision: grouping neighboring white/black pixels into single distinct objects (Connected Component Labeling).
- Physics simulations: modeling fluid filtration through porous stone (percolation theory).
"""

class DisjointSetUnion:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n

    def find(self, x: int) -> int:
        # Path compression: flattens the tree directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # Already in same group

        # Union by rank: attach shorter tree under taller tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.num_components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    dsu = DisjointSetUnion(5)
    dsu.union(0, 1)
    dsu.union(1, 2)
    print("Are 0 and 2 connected?", dsu.connected(0, 2))
    print("Are 0 and 3 connected?", dsu.connected(0, 3))
    print("Remaining groups:", dsu.num_components)
