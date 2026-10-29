"""
Merge Sort Algorithm
====================

What It Does:
-------------
Merge Sort is a sorting algorithm that follows the "divide and conquer" approach.
Simply put:
1. It splits a list into two equal halves.
2. It keeps splitting each half until every piece is just a single item (or empty).
3. Then, it carefully glues (merges) the pieces back together in sorted order.

Use Cases:
----------
- Sorting large datasets where consistent, predictable speed is needed (guaranteed O(n log n)).
- Sorting linked lists (it doesn't require random access memory).
- External sorting (when data is too large to fit in RAM and must be sorted from hard disk/storage).
- Situations where maintaining the relative order of duplicate items matters ("stable sort").
"""


def merge_sort(arr: list[int]) -> list[int]:
    # Base case: a list of 0 or 1 item is already sorted
    if len(arr) <= 1:
        return arr

    # 1. DIVIDE: Find the midpoint and split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. CONQUER: Recursively sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # 3. COMBINE: Merge the two sorted halves into one sorted list
    return merge(sorted_left, sorted_right)


def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = 0  # pointer for left list
    j = 0  # pointer for right list

    # Compare items from both lists and take the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from either list
    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", sample)
    sorted_sample = merge_sort(sample)
    print("Sorted list:  ", sorted_sample)
