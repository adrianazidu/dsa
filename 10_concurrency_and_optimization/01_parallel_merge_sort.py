"""
ALGORITHM: Multithreaded / Parallel Sorting (Parallel Merge Sort)

WHAT IT DOES (SIMPLY):
If you have a giant stack of exam papers to sort alphabetically, one person doing it alone
is slow. Instead, you cut the stack in half, hand each half to a different person to sort
simultaneously (parallel processing), and then quickly merge the two sorted halves together.
This utilizes multiple CPU cores on your computer at the same time.

REAL-LIFE USE CASES:
- Big Data Engines: Sorting billions of transactions in Apache Spark, Hadoop, and database clusters.
- High-Frequency Trading: Processing millions of live stock price ticks per second across server cores.
- Video Game Engines: Updating physics calculations and sorting rendering layers across worker threads.
"""

# Import ProcessPoolExecutor to distribute CPU-bound partitions across physical cores
from concurrent.futures import ProcessPoolExecutor
import random


# Merge function to combine two sorted lists
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Sequential merge sort used below the partition threshold
def sequential_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sequential_merge_sort(arr[:mid])
    right = sequential_merge_sort(arr[mid:])
    return merge(left, right)


# Parallel merge sort using multiprocessing pool
def parallel_merge_sort(arr, executor=None, threshold=2000):
    # Switch to sequential execution for small chunks
    if len(arr) <= threshold:
        return sequential_merge_sort(arr)

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    if executor is None:
        with ProcessPoolExecutor() as new_executor:
            f_left = new_executor.submit(
                parallel_merge_sort, left_half, new_executor, threshold
            )
            f_right = new_executor.submit(
                parallel_merge_sort, right_half, new_executor, threshold
            )
            return merge(f_left.result(), f_right.result())
    else:
        f_left = executor.submit(
            parallel_merge_sort, left_half, executor, threshold
        )
        sorted_right = parallel_merge_sort(right_half, executor, threshold)
        return merge(f_left.result(), sorted_right)


if __name__ == "__main__":
    nums = [random.randint(0, 50000) for _ in range(4000)]
    sorted_nums = parallel_merge_sort(nums, threshold=1000)
    print(f"Array successfully sorted: {sorted_nums == sorted(nums)}")
