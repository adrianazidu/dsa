"""
Binary Search Algorithm
=======================

What It Does:
-------------
Binary Search is a fast search method for sorted collections.
Simply put:
1. It looks at the middle element of the list.
2. If the middle element is what you are looking for, it stops.
3. If your target is smaller, it throws away the entire right half and searches only the left.
4. If your target is larger, it throws away the entire left half and searches only the right.
5. It repeats this halving process until the target is found or there is nowhere left to look.

Use Cases:
----------
- Searching through dictionaries, phonebooks, or alphabetically sorted registries.
- Database index lookups (finding rows quickly using a sorted index column).
- Finding roots or boundaries in games/graphics (e.g., ray marching, finding collision points).
- Git bisect (finding the exact commit that introduced a bug).
"""


def binary_search(arr: list[int], target: int, low: int, high: int) -> int:
    # Base case: search range is invalid, target doesn't exist in the list
    if low > high:
        return -1

    # Pick the middle position
    mid = (low + high) // 2

    # Check if we hit the target right away
    if arr[mid] == target:
        return mid
    # If target is smaller, look only in the left half
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    # If target is larger, look only in the right half
    else:
        return binary_search(arr, target, mid + 1, high)


if __name__ == "__main__":
    sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    index = binary_search(sorted_data, target, 0, len(sorted_data) - 1)
    print(f"List: {sorted_data}")
    print(f"Target {target} found at index: {index}")
