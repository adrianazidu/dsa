"""
Binary Search Trees & Red-Black Trees
-------------------------------------
What it does:
- Binary Search Tree (BST): Organizes numbers so smaller values go left and larger values go right. Makes searching fast on average.
- Red-Black Tree: An enhanced self-balancing BST. By coloring nodes Red or Black and rotating branches when trees get lopsided, it guarantees that lookups, insertions, and deletions stay fast even in the worst case.

Real-World Use Cases:
- Red-Black Trees are used in the Linux process scheduler (Completely Fair Scheduler) to choose which task runs next.
- The foundation of sorted maps and sets in C++ (`std::map`), Java (`TreeMap`), and Python third-party btree libraries.
- Keeping live databases indexed and sorted during continuous inserts.
"""

class BSTNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key: int):
        def _insert(node, val):
            if node is None:
                return BSTNode(val)
            if val < node.key:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, key)

    def search(self, key: int) -> bool:
        curr = self.root
        while curr:
            if curr.key == key: return True
            curr = curr.left if key < curr.key else curr.right
        return False

    def in_order(self) -> list:
        res = []
        def _walk(node):
            if node:
                _walk(node.left)
                res.append(node.key)
                _walk(node.right)
        _walk(self.root)
        return res

if __name__ == "__main__":
    bst = BinarySearchTree()
    for num in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(num)
    print("In-order sorted traversal:", bst.in_order())
    print("Search 40:", bst.search(40))
    print("Search 99:", bst.search(99))
