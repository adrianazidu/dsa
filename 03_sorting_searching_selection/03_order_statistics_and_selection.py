"""
Order Statistics & Linear-Time Selection
----------------------------------------
What it does:
- Simultaneous Min/Max: Finds both the smallest and largest numbers in a list using pairing tricks to do it in roughly 1.5n comparisons instead of 2n.
- Randomized Select (QuickSelect): Finds the k-th smallest item in expected linear time by discarding unneeded partitions.
- Median-of-Medians (BFPRT): Guarantees finding the k-th smallest item in strictly linear time even in the worst case by picking carefully chosen pivots.

Real-World Use Cases:
- Calculating 3D bounding boxes in computer graphics (finding min/max coordinates simultaneously).
- Calculating percentiles and median response times in backend servers (e.g., finding the 95th percentile latency).
- Operating system safety fallbacks (C++ `std::nth_element` uses median-of-medians as a fail-safe if standard selection takes too long).
"""

# 1. Simultaneous Min and Max
def find_min_max(arr: list[int]) -> tuple[int, int]:
    if not arr: raise ValueError("List cannot be empty")
    n = len(arr)
    if n % 2 != 0:
        c_min = c_max = arr[0]
        start = 1
    else:
        c_min, c_max = (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
        start = 2

    for i in range(start, n - 1, 2):
        if arr[i] < arr[i + 1]:
            if arr[i] < c_min: c_min = arr[i]
            if arr[i + 1] > c_max: c_max = arr[i + 1]
        else:
            if arr[i + 1] < c_min: c_min = arr[i + 1]
            if arr[i] > c_max: c_max = arr[i]
    return c_min, c_max

# 2. Median-of-Medians (Worst-Case Linear Selection)
def median_of_medians_select(arr: list[int], k: int) -> int:
    if len(arr) <= 5:
        return sorted(arr)[k - 1]
    # Split into groups of 5 and find medians
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(g)[len(g) // 2] for g in groups]
    # Recursively find median of the medians
    pivot = median_of_medians_select(medians, (len(medians) + 1) // 2)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k <= len(lows):
        return median_of_medians_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return median_of_medians_select(highs, k - len(lows) - len(pivots))

if __name__ == "__main__":
    nums = [19, 3, 14, 28, 5, 33, 8, 1]
    print("Min and Max:", find_min_max(nums))
    k = 4  # 4th smallest
    print(f"{k}-th smallest via Median-of-Medians:", median_of_medians_select(nums, k))
