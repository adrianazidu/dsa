"""
Elementary Data Structures
--------------------------
What it does:
- Singly Linked List: Nodes chained together using memory references (pointers). Adding or removing items at known locations is very fast.
- Stack (LIFO): Last-In, First-Out container. Like a stack of plates—you can only add or remove from the top.
- Queue (FIFO): First-In, First-Out container. Like a line at a grocery checkout—first person to arrive is first to be served.
- Hash Table: Uses a hash function to turn keys into bucket numbers. Provides near-instant lookups, insertions, and deletions.

Real-World Use Cases:
- Linked Lists: Memory management inside operating systems, building undo/redo buffers.
- Stacks: Managing function calls in programming languages, matching parentheses in code editors.
- Queues: Print queues, web server request processing, job scheduling pipelines.
- Hash Tables: Database caching (Redis), fast dictionary lookups, user session management.
"""

from collections import deque

# 1. Singly Linked List
class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val: int):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def to_list(self) -> list:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

# 2. Stack (LIFO)
class Stack:
    def __init__(self):
        self._items = []

    def push(self, val):
        self._items.append(val)

    def pop(self):
        if not self._items: raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self):
        return self._items[-1] if self._items else None

# 3. Queue (FIFO)
class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, val):
        self._items.append(val)

    def dequeue(self):
        if not self._items: raise IndexError("Queue is empty")
        return self._items.popleft()

# 4. Hash Table (Chaining)
class SimpleHashTable:
    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key: str) -> int:
        return hash(key) % self.capacity

    def put(self, key: str, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))

    def get(self, key: str):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        raise KeyError(f"Key {key} not found")

if __name__ == "__main__":
    s = Stack()
    s.push(10); s.push(20)
    print("Stack pop (LIFO):", s.pop())

    q = Queue()
    q.enqueue("Alice"); q.enqueue("Bob")
    print("Queue dequeue (FIFO):", q.dequeue())

    ht = SimpleHashTable()
    ht.put("user_1", "Alice")
    print("Hash Table lookup:", ht.get("user_1"))
