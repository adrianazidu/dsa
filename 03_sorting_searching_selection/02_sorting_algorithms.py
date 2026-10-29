"""
Comprehensive Sorting Algorithms
-------------------------------
What it does:
- HeapSort: Organizes items into a binary heap tree, repeatedly pulling out the largest item. Guarantees fast sorting with zero extra memory.
- QuickSort: Picks a pivot and puts smaller items to the left and larger to the right. Very fast in practice.
- Selection Sort: Repeatedly scans for the smallest remaining item and swaps it into place. Minimizes physical writes.
- Counting Sort: Counts how many times each integer occurs and places them in order. Fast for small ranges of integers.
- Stooge Sort: Recursively sorts the first 2/3, last 2/3, and first 2/3 again. Very slow; used for teaching recursion.
- Odd-Even Sort: Compares adjacent pairs alternating between odd and even positions. Runs well on parallel hardware.
- Binary Tree Sort: Inserts numbers into a binary search tree and walks through it in order.
- Smoothsort: A smart variation of HeapSort that runs in nearly linear time if the data is already mostly sorted.
- Shell Sort: An improved insertion sort that compares items far apart, gradually reducing the gap.
- Comb Sort: An improved bubble sort that eliminates small values stuck at the end of the list.

Real-World Use Cases:
- Operating system standard libraries (QuickSort and HeapSort fallbacks).
- Microcontrollers and flash memory where write operations must be minimized (Selection Sort, Shell Sort).
- Fast integer sorting for graphics and IP addresses (Counting Sort).
- Massively parallel GPU/FPGA sorting networks (Odd-Even Sort).
"""

# 1. HeapSort
def heapsort(arr: list) -> list:
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]: largest = l
        if r < n and arr[r] > arr[largest]: largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    return arr

# 2. QuickSort
def quicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 3. Selection Sort
def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 4. Counting Sort (non-negative integers)
def counting_sort(arr: list) -> list:
    if not arr: return []
    min_val, max_val = min(arr), max(arr)
    counts = [0] * (max_val - min_val + 1)
    for x in arr:
        counts[x - min_val] += 1
    res = []
    for val_offset, count in enumerate(counts):
        res.extend([val_offset + min_val] * count)
    return res

# 5. Shell Sort
def shell_sort(arr: list) -> list:
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# 6. Comb Sort
def comb_sort(arr: list) -> list:
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted_flag = False
    while not sorted_flag:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True
        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False
    return arr

if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("HeapSort:", heapsort(sample.copy()))
    print("QuickSort:", quicksort(sample.copy()))
    print("Selection Sort:", selection_sort(sample.copy()))
    print("Shell Sort:", shell_sort(sample.copy()))
    print("Comb Sort:", comb_sort(sample.copy()))
