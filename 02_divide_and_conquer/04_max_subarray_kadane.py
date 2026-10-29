"""
Maximum Subarray (Kadane's Algorithm)
=====================================

What It Does:
-------------
Kadane's Algorithm is the fastest and most efficient way to solve the Maximum Subarray problem.
Simply put:
1. It walks through the list from left to right just once.
2. It keeps adding numbers to a running total.
3. If the running total ever drops below zero, it discards it and starts fresh from the next number
   (because starting with a negative total can only drag down future sums).
4. Meanwhile, it keeps track of the highest running total it ever reached.

Use Cases:
----------
- Real-time stock trading & financial streak analysis (instant 1-pass execution).
- Audio signal processing: locating bursts of loudest continuous sound waves.
- Gaming / UI: detecting longest streak of high player performance or bonus multipliers.
- Anywhere you need maximum subarray sum with minimum memory and speed (O(n) time, O(1) space).
"""

from typing import Tuple


def max_subarray_kadane(nums: list[int]) -> Tuple[int, int, int]:
    # Highest sum seen anywhere so far
    max_so_far = float("-inf")
    # Current running sum of our active window
    current_sum = 0

    start = 0
    end = 0
    temp_start = 0

    for i, num in enumerate(nums):
        current_sum += num

        # If we reached a new peak, record the score and window boundaries
        if current_sum > max_so_far:
            max_so_far = current_sum
            start = temp_start
            end = i

        # If current total drops into negative territory, reset
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return start, end, max_so_far


if __name__ == "__main__":
    sample = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    start, end, max_val = max_subarray_kadane(sample)
    print("Array:", sample)
    print(f"Max Subarray starts at {start}, ends at {end}, sum = {max_val}")
    print(f"Winning slice: {sample[start:end+1]}")
