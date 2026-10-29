"""
Probabilistic Analysis & Randomized Algorithms
---------------------------------------------
What it does:
- Fisher-Yates Shuffle (Randomize-in-Place): Takes a list and shuffles it uniformly at random so every possible ordering has an equal chance of appearing.
- The Hiring Problem: Simulates interviewing candidates in random order and only hiring someone if they are better than everyone seen before. Probabilistic analysis shows you only hire around ln(n) times.
- Randomized QuickSort: Sorts a list by picking a random pivot element. Randomizing the pivot prevents bad/adversarial inputs from slowing down the algorithm.

Real-World Use Cases:
- Shuffling decks of cards in online poker and casino platforms without bias.
- Randomly assigning patients to test vs. control groups in medical trials.
- Shuffling machine learning datasets between training epochs.
- Fast, secure data sorting in operating systems and backend services.
"""

import random
import math

# 1. Fisher-Yates Shuffle
def randomize_in_place(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        # Pick a random index between i and the end of the list
        random_index = random.randint(i, n - 1)
        # Swap current item with the random item
        arr[i], arr[random_index] = arr[random_index], arr[i]
    return arr

# 2. Hiring Problem Simulation
def simulate_hiring(candidates: list) -> tuple[int, int]:
    # Randomize candidate interview order
    randomize_in_place(candidates)
    best_quality = float("-inf")
    hire_count = 0
    for quality in candidates:
        if quality > best_quality:
            best_quality = quality
            hire_count += 1
    return hire_count, best_quality

# 3. Randomized QuickSort
def randomized_partition(arr: list, low: int, high: int) -> int:
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr: list, low: int, high: int) -> None:
    if low < high:
        pivot_idx = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_idx - 1)
        randomized_quicksort(arr, pivot_idx + 1, high)

if __name__ == "__main__":
    nums = [42, 17, 89, 8, 23, 64, 5]
    print("Original:", nums)
    randomize_in_place(nums)
    print("Shuffled:", nums)
    randomized_quicksort(nums, 0, len(nums) - 1)
    print("Sorted with Randomized QuickSort:", nums)
