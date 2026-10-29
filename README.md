# Data Structures & Algorithms in Python

A hands-on collection of classic data structures and algorithms, written in plain Python with
beginner-friendly explanations and real-world use cases in every file.

Folders are numbered from **basic to advanced**, and the files inside each folder are numbered
in the recommended reading order.

For a big data scenario showing *why* and *how* each algorithm is used, see
[USE_CASES.md](USE_CASES.md).

## How to run

Everything uses only the Python standard library, so there is nothing to install.
Each file is a self-contained demo:

```bash
python 02_divide_and_conquer/02_merge_sort.py
```

---

## 01 · Foundations

| File | What it does |
|---|---|
| [01_big_o.txt](01_foundations/01_big_o.txt) | Notes introducing Big-O notation and time complexity.<br>Explains that complexity counts steps, not seconds on a specific machine. |
| [02_recurrence_tracker.py](01_foundations/02_recurrence_tracker.py) | Simulates the recurrence T(n) = 2T(n/2) + n by counting operations level by level.<br>Lets you see with your own eyes how divide-and-conquer work scales with input size. |
| [03_master_theorem_solver.py](01_foundations/03_master_theorem_solver.py) | Solves recurrences of the form T(n) = aT(n/b) + O(n^d) using the Master Theorem.<br>Tells you whether the leaves, the root, or every level dominates the running time. |
| [04_amortized_analysis.py](01_foundations/04_amortized_analysis.py) | Demonstrates dynamic array resizing, a multi-pop stack and a binary counter.<br>Shows why rare expensive steps still average out to O(1) per operation. |

## 02 · Divide and Conquer

| File | What it does |
|---|---|
| [01_binary_search.py](02_divide_and_conquer/01_binary_search.py) | Finds a target in a sorted list by repeatedly halving the search range.<br>Runs in O(log n), the idea behind database indexes and `git bisect`. |
| [02_merge_sort.py](02_divide_and_conquer/02_merge_sort.py) | Splits a list into halves, sorts each recursively, then merges them back in order.<br>A stable O(n log n) sort and the textbook example of divide and conquer. |
| [03_max_subarray_divide_and_conquer.py](02_divide_and_conquer/03_max_subarray_divide_and_conquer.py) | Finds the contiguous slice with the largest sum by checking the left, right and crossing halves.<br>Runs in O(n log n) and shows how to combine results from subproblems. |
| [04_max_subarray_kadane.py](02_divide_and_conquer/04_max_subarray_kadane.py) | Solves the same maximum-subarray problem in a single O(n) pass (Kadane's algorithm).<br>Keeps a running total and restarts whenever the total drops below zero. |

## 03 · Sorting, Searching and Selection

| File | What it does |
|---|---|
| [01_searching_algorithms.py](03_sorting_searching_selection/01_searching_algorithms.py) | Implements linear search, binary search and jump search.<br>Compares when each one fits: unsorted data, sorted data, or slow-to-seek storage. |
| [02_sorting_algorithms.py](03_sorting_searching_selection/02_sorting_algorithms.py) | Implements HeapSort, QuickSort, Selection, Counting, Stooge, Odd-Even, Tree Sort and Smoothsort.<br>A side-by-side tour of the trade-offs between speed, memory and stability. |
| [03_order_statistics_and_selection.py](03_sorting_searching_selection/03_order_statistics_and_selection.py) | Finds min/max together, and the k-th smallest item with QuickSelect and Median-of-Medians.<br>Gets medians and percentiles in linear time without sorting the whole list. |

## 04 · Data Structures

| File | What it does |
|---|---|
| [01_stack.py](04_data_structures/01_stack.py) | A simple list-based stack with push, pop and an empty check.<br>Demonstrates the Last-In, First-Out (LIFO) principle with O(1) operations. |
| [02_linked_list.py](04_data_structures/02_linked_list.py) | Builds a singly linked list by chaining nodes from a HEAD pointer.<br>Traverses and prints the list node by node until it reaches the end. |
| [03_elementary_data_structures.py](04_data_structures/03_elementary_data_structures.py) | Implements a singly linked list, a stack, a queue and a hash table.<br>The core building blocks behind function calls, task queues and fast lookups. |
| [04_disjoint_set_union.py](04_data_structures/04_disjoint_set_union.py) | Union-Find with path compression and union by rank.<br>Tracks groups of connected items and merges them in near-constant time. |
| [05_trees_and_balanced_search_trees.py](04_data_structures/05_trees_and_balanced_search_trees.py) | Implements a Binary Search Tree and a self-balancing Red-Black Tree.<br>Rotations and node colors keep lookups O(log n) even in the worst case. |
| [06_augmenting_data_structures.py](04_data_structures/06_augmenting_data_structures.py) | Adds extra data to tree nodes to build an Order-Statistic Tree and an Interval Tree.<br>Answers rank queries and overlap checks (such as calendar conflicts) in O(log n). |
| [07_advanced_trees_and_heaps.py](04_data_structures/07_advanced_trees_and_heaps.py) | Introduces B-Trees, Fibonacci Heaps and van Emde Boas Trees.<br>Specialized structures that power databases, file systems and fast routing. |

## 05 · Algorithm Design Techniques

| File | What it does |
|---|---|
| [01_greedy_algorithms.py](05_design_techniques/01_greedy_algorithms.py) | Fractional knapsack, activity selection, Huffman coding and Kruskal's MST.<br>Each makes the best local choice at every step, and still reaches an optimal answer. |
| [02_dynamic_programming.py](05_design_techniques/02_dynamic_programming.py) | 0/1 knapsack, Longest Common Subsequence and Bellman-Ford shortest paths.<br>Solves each subproblem once and stores the answer in a table to avoid repeated work. |

## 06 · Randomized Algorithms

| File | What it does |
|---|---|
| [01_probabilistic_and_randomized.py](06_randomized_algorithms/01_probabilistic_and_randomized.py) | Fisher-Yates shuffle, the hiring problem and randomized QuickSort.<br>Shows how randomness gives unbiased results and protects against bad inputs. |
| [02_las_vegas_and_monte_carlo.py](06_randomized_algorithms/02_las_vegas_and_monte_carlo.py) | Compares Las Vegas (randomized QuickSelect) with Monte Carlo (Pi estimation, Fermat primality test).<br>One is always correct with a random runtime; the other has a fixed runtime with an approximate answer. |
| [03_monte_carlo_tree_search.py](06_randomized_algorithms/03_monte_carlo_tree_search.py) | Monte Carlo Tree Search: selection, expansion, random rollouts and backpropagation.<br>Balances exploration and exploitation to choose moves, as in game AIs like AlphaGo. |

## 07 · Graph Algorithms

| File | What it does |
|---|---|
| [01_graph_fundamentals.py](07_graph_algorithms/01_graph_fundamentals.py) | BFS, DFS, topological sort, Dijkstra, Floyd-Warshall, Kosaraju SCC and Edmonds-Karp.<br>A broad overview of the core graph algorithms in one file. |
| [02_minimum_spanning_tree.py](07_graph_algorithms/02_minimum_spanning_tree.py) | Kruskal's algorithm connects every node with the minimum total edge cost.<br>Repeatedly picks the cheapest edge that doesn't form a loop, as when laying network cable. |
| [03_single_source_shortest.py](07_graph_algorithms/03_single_source_shortest.py) | Dijkstra's algorithm finds the shortest path from one start node to all others.<br>Always explores the closest unvisited node next, like GPS route planning. |
| [04_all_pairs_shortest.py](07_graph_algorithms/04_all_pairs_shortest.py) | Floyd-Warshall computes shortest distances between every pair of nodes.<br>Tests whether a detour through each intermediate node shortens any path. |
| [05_maximum_flow.py](07_graph_algorithms/05_maximum_flow.py) | Edmonds-Karp (Ford-Fulkerson with BFS) finds the maximum flow from source to sink.<br>Keeps pushing flow along paths with spare capacity until the network hits its bottleneck. |

## 08 · Strings and Geometry

| File | What it does |
|---|---|
| [01_kmp_string_matching.py](08_strings_and_geometry/01_kmp_string_matching.py) | Knuth-Morris-Pratt pattern matching in O(n + m) time.<br>Pre-processes the pattern so a mismatch never forces re-reading the text. |
| [02_convex_hull_graham.py](08_strings_and_geometry/02_convex_hull_graham.py) | Graham Scan finds the convex hull, the "rubber band" boundary around a set of points.<br>Walks the perimeter and discards any point that creates an inward dent. |

## 09 · Algebra and Cryptography

| File | What it does |
|---|---|
| [01_rsa_number_theory.py](09_algebra_and_cryptography/01_rsa_number_theory.py) | Number-theory tools (GCD, primality testing, modular math) that build a mini RSA system.<br>Generates keys, then encrypts and decrypts messages with public-key cryptography. |
| [02_fast_fourier_transform.py](09_algebra_and_cryptography/02_fast_fourier_transform.py) | Fast Fourier Transform used for fast polynomial multiplication.<br>Converts coefficients to frequency points, multiplies them, then converts back in O(n log n). |

## 10 · Concurrency and Optimization

| File | What it does |
|---|---|
| [01_parallel_merge_sort.py](10_concurrency_and_optimization/01_parallel_merge_sort.py) | Merge sort that sorts halves at the same time on multiple CPU cores.<br>Uses `ProcessPoolExecutor` to show how parallelism speeds up large sorts. |
| [02_matrix_lu_inversion.py](10_concurrency_and_optimization/02_matrix_lu_inversion.py) | Matrix inversion via LU decomposition (lower and upper triangular factors).<br>Turns a large system of equations into simple step-by-step substitutions. |
| [03_simplex_solver.py](10_concurrency_and_optimization/03_simplex_solver.py) | Dantzig's Simplex algorithm for linear programming.<br>Walks the corners of the feasible region toward the best profit or lowest cost. |

## 11 · NP-Completeness and Approximation

| File | What it does |
|---|---|
| [01_vertex_cover_approx.py](11_np_and_approximation/01_vertex_cover_approx.py) | A 2-approximation for the NP-complete Vertex Cover problem.<br>Runs fast and guarantees at most twice the minimum number of chosen nodes. |
| [02_metric_tsp_approx.py](11_np_and_approximation/02_metric_tsp_approx.py) | A 2-approximation for the metric Traveling Salesperson Problem, built from a minimum spanning tree.<br>Shortcuts a tree walk so the tour is never more than twice the optimal length. |

---

## License

See [LICENSE](LICENSE).
