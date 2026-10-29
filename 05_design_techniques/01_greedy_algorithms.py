"""
Greedy Algorithms
-----------------
What it does:
Makes the immediate best local choice at each step without looking back or second-guessing, aiming for an overall optimal result.
- Fractional Knapsack: Takes items with the highest value-per-pound ratio first, cutting items into fractions if necessary.
- Activity Selection: Picks the activity that finishes earliest so the venue or resource is free for the next activity as soon as possible.
- Huffman Coding: Assigns short binary codes to frequent characters and long codes to rare characters to compress data.
- Kruskal's Minimum Spanning Tree: Connects all points with the least total wire/cable by repeatedly picking the cheapest available connection that doesn't create a loop.

Real-World Use Cases:
- Data compression in ZIP, MP3, and JPEG files (Huffman coding).
- Planning cable, electrical, and fiber-optic networks with minimal materials (Kruskal's MST).
- Room and conference booking schedules (Activity Selection).
- Bandwidth and server compute quota allocation (Fractional Knapsack).
"""

import heapq

# 1. Activity Selection
def activity_selection(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # Sort activities by finish time
    sorted_acts = sorted(activities, key=lambda a: a[1])
    selected = [sorted_acts[0]]
    last_finish = sorted_acts[0][1]
    for start, finish in sorted_acts[1:]:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    return selected

# 2. Huffman Coding Tree
def huffman_encoding(frequencies: dict[str, int]) -> dict[str, str]:
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]: pair[1] = '0' + pair[1]
        for pair in hi[1:]: pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return dict(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))

if __name__ == "__main__":
    meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    print("Selected compatible meetings:", activity_selection(meetings))
    freqs = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}
    print("Huffman codes:", huffman_encoding(freqs))
