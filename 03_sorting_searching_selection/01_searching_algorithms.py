"""
Search Algorithms
-----------------
What it does:
- Linear Search: Scans items one by one from beginning to end until it finds a match. Simple and works on unsorted lists.
- Binary Search: Works on sorted lists. Looks at the middle element and cuts the remaining search area in half each step. Extremely fast.
- Jump Search: Works on sorted lists. Jumps ahead by fixed blocks (step size = sqrt(n)), then walks backward one by one once it overshoots.

Real-World Use Cases:
- Linear Search: Small lists (under 50 items) or continuous streaming data that hasn't been sorted.
- Binary Search: Looking up records in database indexes, checking dictionaries, or finding which commit broke code via `git bisect`.
- Jump Search: Searching large sorted files on magnetic tape drives or network drives where jumping backward is slow and expensive.
"""

import math

def linear_search(arr: list, target: int) -> int:
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1

def binary_search(arr: list, target: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def jump_search(arr: list, target: int) -> int:
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        if arr[prev] > target:
            return -1
        prev += 1
    return -1

if __name__ == "__main__":
    sorted_items = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    print("Linear Search index:", linear_search(sorted_items, target))
    print("Binary Search index:", binary_search(sorted_items, target))
    print("Jump Search index:", jump_search(sorted_items, target))
