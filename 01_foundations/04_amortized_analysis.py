"""
Amortized Analysis
------------------
What it does:
Analyzes operations where an occasional step is very slow and expensive, but happens so rarely that the average cost per operation over time remains small and constant.
- Dynamic Array Resizing: Inserting into an array is usually instant, but occasionally requires allocating a bigger array and copying everything over. Amortized analysis proves that every insert costs only O(1) on average.
- Multi-Pop Stack: Pushing is fast; popping multiple items at once can take time, but you cannot pop more items than you pushed.
- Binary Counter: Flipping bits during increments. Cascading carries are rare, making increments cost O(1) amortized.

Real-World Use Cases:
- The resizing strategy used in Python lists (`list.append`), C++ vectors (`std::vector::push_back`), and Java `ArrayList`.
- Text editor undo buffers and bulk delete operations.
- Digital clock dividers and processor counter circuits.
"""

class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity
        self.total_actual_work = 0

    def append(self, element: int) -> int:
        actual_work = 1
        if self.size == self.capacity:
            # Expensive step: allocate double capacity and copy
            new_capacity = self.capacity * 2
            new_data = [None] * new_capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
                actual_work += 1
            self.data = new_data
            self.capacity = new_capacity

        self.data[self.size] = element
        self.size += 1
        self.total_actual_work += actual_work
        return actual_work

if __name__ == "__main__":
    arr = DynamicArray()
    for i in range(1, 9):
        work = arr.append(i)
        print(f"Append #{i:2d} | Cost this step: {work:2d} | Avg cost so far: {arr.total_actual_work / i:.2f}")
