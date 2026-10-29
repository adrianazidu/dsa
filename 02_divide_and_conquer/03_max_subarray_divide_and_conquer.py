"""
Maximum Subarray (Divide and Conquer Approach)
==============================================

What It Does:
-------------
Given a list of positive and negative numbers, this algorithm finds a contiguous
slice (sub-list) that has the highest possible sum.
Simply put:
1. It divides the array in half.
2. The best sequence must live in one of three places:
   - Entirely on the left side.
   - Entirely on the right side.
   - Crossing straight through the middle.
3. It calculates all three possibilities and picks the highest sum.

Use Cases:
----------
- Financial analysis: finding the best consecutive days to buy and sell stocks.
- Computer vision & image processing: finding the brightest continuous region in a sensor line.
- Genomic analysis: identifying the most significant sequence/cluster of high-scoring DNA markers.
- Teaching & academic practice: demonstrating multi-case divide-and-conquer logic.
"""

from typing import Tuple


def find_max_crossing_subarray(
    nums: list[int], low: int, mid: int, high: int
) -> Tuple[int, int, int]:
    # 1. Left side of the cross: walk backwards from mid to low
    left_sum = float("-inf")
    current_sum = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        current_sum += nums[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i

    # 2. Right side of the cross: walk forwards from mid+1 to high
    right_sum = float("-inf")
    current_sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        current_sum += nums[j]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = j

    # Return start index, end index, and the combined sum
    return max_left, max_right, left_sum + right_sum


def max_subarray_divide_and_conquer(
    nums: list[int], low: int, high: int
) -> Tuple[int, int, int]:
    # Base case: only one element
    if low == high:
        return low, high, nums[low]

    # Divide
    mid = (low + high) // 2

    # Conquer (solve both halves)
    left_low, left_high, left_sum = max_subarray_divide_and_conquer(nums, low, mid)
    right_low, right_high, right_sum = max_subarray_divide_and_conquer(nums, mid + 1, high)

    # Combine (check the middle cross)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(nums, low, mid, high)

    # Pick the winner among left, right, and cross
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


if __name__ == "__main__":
    sample = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    start, end, max_val = max_subarray_divide_and_conquer(sample, 0, len(sample) - 1)
    print("Array:", sample)
    print(f"Max Subarray starts at {start}, ends at {end}, sum = {max_val}")
    print(f"Winning slice: {sample[start:end+1]}")
