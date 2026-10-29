"""
Recurrence Work Simulator
=========================

What It Does:
-------------
This script simulates the call structure of a divide-and-conquer recurrence relation
(specifically Merge Sort: T(n) = 2T(n/2) + n) by counting raw operations.
Simply put:
Instead of sorting real values, it tracks how many operations get performed at each level
of recursion so you can see with your own eyes how the work scales as input size grows.

Use Cases:
----------
- Visualizing and demonstrating algorithm growth curves to students or teams.
- Validating theoretical runtime against simulated operation counts.
- Profiling recursive branching overhead in custom algorithms.
"""

import math


class RecurrenceTracker:
    def __init__(self):
        self.operations = 0

    def solve_merge_sort_recurrence(self, n: int) -> int:
        # Base case
        if n <= 1:
            self.operations += 1
            return 1

        # Combine work at current level: O(n)
        self.operations += n

        # Two subproblems of size n // 2
        return (
            self.solve_merge_sort_recurrence(n // 2)
            + self.solve_merge_sort_recurrence(n // 2)
        )


if __name__ == "__main__":
    tracker = RecurrenceTracker()
    test_sizes = [16, 64, 256, 1024]

    print("Empirical Operation Counting vs Theoretical n*log2(n):")
    print("-" * 65)
    for size in test_sizes:
        tracker.operations = 0
        tracker.solve_merge_sort_recurrence(size)
        expected = size * math.log2(size)
        print(
            f"Input Size n = {size:4d} | Operations: {tracker.operations:6d} | Theoretical (n*log2(n)): {expected:8.1f}"
        )
