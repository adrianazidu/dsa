"""
Augmenting Data Structures
--------------------------
What it does:
Takes an existing data structure (like a binary tree) and adds extra metadata to every node so you can answer new questions instantly:
- Order-Statistic Tree: Stores the count of items in each subtree. Allows finding the "k-th smallest element" or finding a number's exact ranking in fast logarithmic time.
- Interval Tree: Stores the maximum upper bound in each subtree. Instantly detects if a time range overlaps with any existing booked range.

Real-World Use Cases:
- Live gaming leaderboards: finding which player is ranked #500 or computing player percentiles.
- Calendar scheduling (Google Calendar / Outlook): checking if a new meeting conflicts with existing appointments.
- Operating system memory management: verifying that newly mapped memory does not overlap with existing allocations.
"""

class OSTNode:
    def __init__(self, key: int):
        self.key = key
        self.size = 1
        self.left = None
        self.right = None

def get_size(node):
    return node.size if node else 0

def update_size(node):
    if node:
        node.size = 1 + get_size(node.left) + get_size(node.right)

def ost_select(node: OSTNode, k: int):
    # Finds the k-th smallest element (1-indexed rank)
    if node is None:
        return None
    left_rank = get_size(node.left) + 1
    if k == left_rank:
        return node.key
    elif k < left_rank:
        return ost_select(node.left, k)
    else:
        return ost_select(node.right, k - left_rank)

if __name__ == "__main__":
    root = OSTNode(30)
    root.left = OSTNode(15)
    root.right = OSTNode(50)
    update_size(root)
    print("2nd smallest element in tree:", ost_select(root, 2))
