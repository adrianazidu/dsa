# Big Data Use Cases

For every file in this repo: a realistic big data situation, **why** that algorithm is the right
tool, and **how** you would apply it. Sections follow the same order as the [README](README.md).

Each entry answers three questions:

- **Situation** – the problem you are facing.
- **Why this algorithm** – what makes it the right choice over the alternatives.
- **How** – the steps you would actually take.

---

## 01 · Foundations

### [01_big_o.txt](01_foundations/01_big_o.txt) — Big-O Notation

**Situation:** Your team wants to deduplicate 1 billion customer records overnight. One engineer
proposes comparing every record with every other record.

**Why this algorithm:** Big-O lets you reject that plan before writing any code. Comparing all pairs is
O(n²), which is about 10¹⁸ comparisons and would take centuries. A sort-based or hash-based approach is
O(n log n) or O(n), which is about 3×10¹⁰ steps and finishes in minutes.

**How:**
1. Count how many times the innermost operation runs as a function of n.
2. Keep only the fastest-growing term (n², n log n, n…).
3. Plug in your real n (10⁹) to estimate total steps, and pick the design that fits your time budget.

### [02_recurrence_tracker.py](01_foundations/02_recurrence_tracker.py) — Recurrence Work Simulator

**Situation:** A recursive job that splits log files in half and merges the results gets slower than
expected as the data grows from 10 GB to 1 TB.

**Why this algorithm:** Counting the work at each recursion level shows *where* the time goes. For
T(n) = 2T(n/2) + n, every level does the same n work across log n levels. If your numbers don't match,
the bug is in your merge step, not in the recursion.

**How:**
1. Model the job as a recurrence (how many sub-jobs, how much smaller, how much merge work).
2. Run the simulator for growing n and record the operations per level.
3. Compare the measured growth with the prediction to find the level that misbehaves.

### [03_master_theorem_solver.py](01_foundations/03_master_theorem_solver.py) — Master Theorem

**Situation:** You are designing a recursive aggregation for a distributed analytics engine. It can split
the data into 4 parts at a quarter of the size each, or into 2 parts at half the size each, with
different merge costs.

**Why this algorithm:** The Master Theorem gives the overall complexity of each design in seconds, so you
can choose before you build. It tells you whether the leaves (the data scan) or the root (the final merge)
will dominate.

**How:**
1. Write each design as T(n) = aT(n/b) + O(n^d).
2. Enter a, b and d into the solver.
3. Pick the design with the lowest growth rate. If the root dominates, optimize the merge step.

### [04_amortized_analysis.py](01_foundations/04_amortized_analysis.py) — Amortized Analysis

**Situation:** An ingestion service appends millions of clickstream events per second into in-memory
buffers. Occasionally a buffer has to grow and copy everything, which causes latency spikes.

**Why this algorithm:** Amortized analysis proves that doubling the buffer size keeps the *average* cost
per append at O(1), even though a single resize is O(n). It also explains why growing by a fixed amount
(say +1000 slots) would be O(n) per append, which is a disaster at this scale.

**How:**
1. Use a dynamic array that doubles its capacity when full, like Python's `list`.
2. If the occasional spike is unacceptable, preallocate based on the expected batch size.
3. Monitor the throughput averaged over many appends rather than single-operation latency.

---

## 02 · Divide and Conquer

### [01_binary_search.py](02_divide_and_conquer/01_binary_search.py) — Binary Search

**Situation:** You store 10 billion log entries in sorted, time-ordered files and need to find the first
entry after `2026-10-29 14:00:00`.

**Why this algorithm:** Data that is already sorted lets you jump straight to the answer. Binary search
needs about 34 steps for 10 billion entries, while a linear scan reads everything. This is how
Parquet/ORC row-group indexes, Kafka offset lookups and `git bisect` work.

**How:**
1. Make sure the data is sorted by the key you query (here, the timestamp).
2. Look at the middle entry and drop the half that cannot contain the target.
3. Repeat until one entry remains, then read forward from there.

### [02_merge_sort.py](02_divide_and_conquer/02_merge_sort.py) — Merge Sort

**Situation:** You need to sort 2 TB of transaction records by customer ID on a machine with only 64 GB
of RAM.

**Why this algorithm:** Merge sort is the basis of *external sorting*. It works on sorted chunks and merges
them sequentially, so it never needs all the data in memory. It also reads disk sequentially, which is fast.
It is stable and guaranteed O(n log n), so there are no bad-case surprises.

**How:**
1. Read chunks that fit in RAM (for example 32 GB), sort each one and write it back to disk as a "run".
2. Open all the runs and merge them, always writing out the smallest current head (a k-way merge).
3. The result is one fully sorted file. Hadoop and Spark shuffles use the same pattern.

### [03_max_subarray_divide_and_conquer.py](02_divide_and_conquer/03_max_subarray_divide_and_conquer.py) — Max Subarray (Divide and Conquer)

**Situation:** You have years of daily profit and loss data split across many servers. You want the
contiguous period with the highest total gain.

**Why this algorithm:** The divide-and-conquer version parallelizes naturally. Each server solves its own
time range, and the results combine through the "crossing" case at the boundaries, so no machine needs the
whole series.

**How:**
1. Give each worker a contiguous time range and have it compute its best subarray, best prefix, best
   suffix and total.
2. Combine neighboring results: the best is the left best, the right best, or the left suffix plus the
   right prefix.
3. Repeat the combine step up a tree until one answer remains.

### [04_max_subarray_kadane.py](02_divide_and_conquer/04_max_subarray_kadane.py) — Kadane's Algorithm

**Situation:** A live stream of per-minute server error deltas arrives and you want to detect the worst
continuous incident window as it happens.

**Why this algorithm:** Kadane's algorithm is a single O(n) pass with O(1) memory. It processes each value
once and never looks back, which is exactly what a stream needs.

**How:**
1. Keep a running sum and a best-so-far sum.
2. For each new value, add it to the running sum. If the running sum drops below zero, reset it.
3. Whenever the running sum beats the best, record the window and raise an alert if it crosses a
   threshold.

---

## 03 · Sorting, Searching and Selection

### [01_searching_algorithms.py](03_sorting_searching_selection/01_searching_algorithms.py) — Linear, Binary and Jump Search

**Situation:** A data platform stores some data unsorted (a fresh ingest buffer), some sorted in memory
(an index) and some sorted on slow network storage where seeking backward is expensive.

**Why this algorithm:** Each storage type needs a different search:
- **Linear search** is the only option for the unsorted buffer, and is fine because the buffer is small.
- **Binary search** is best for the sorted in-memory index (O(log n)).
- **Jump search** suits slow sequential media: it jumps forward in √n blocks and only scans a small block
  at the end.

**How:**
1. Classify each data source as unsorted, sorted with random access, or sorted with sequential access.
2. Route each query to the matching search function.
3. Benchmark on real data, since for small n the simple linear scan often wins because of CPU caching.

### [02_sorting_algorithms.py](03_sorting_searching_selection/02_sorting_algorithms.py) — Sorting Algorithms

**Situation:** A pipeline sorts several kinds of data: billions of event records, 8-bit sensor readings,
nearly sorted time series from late-arriving events, and data on GPU-style parallel hardware.

**Why this algorithm:** No single sort is best everywhere:
- **QuickSort**: the fastest general-purpose in-memory sort in practice.
- **HeapSort**: guaranteed O(n log n) with no extra memory, for memory-tight workers.
- **Counting Sort**: O(n + k) for small integer ranges like 0–255 sensor values. It beats any comparison sort.
- **Smoothsort**: close to O(n) on nearly sorted data such as time series with a few late events.
- **Odd-Even Sort**: every comparison in a pass is independent, which suits parallel hardware.
- **Binary Tree Sort**: sorts as data arrives by inserting into a BST.
- **Selection Sort**: minimizes writes, which matters on flash storage with limited write cycles.
- **Stooge Sort**: teaching only, never for production.

**How:**
1. Profile the data: its size, key type and range, and whether it's already partly sorted.
2. Pick the matching algorithm from the list above.
3. In production, prefer the language's built-in sort (Timsort in Python) unless you have a special case
   like small integer keys.

### [03_order_statistics_and_selection.py](03_sorting_searching_selection/03_order_statistics_and_selection.py) — Order Statistics and Selection

**Situation:** Every minute you must report the median and p95 latency across 500 million API requests.

**Why this algorithm:** You don't need the whole list sorted, only the item at rank k. QuickSelect finds it
in expected O(n), compared with O(n log n) for sorting. Median-of-Medians guarantees O(n) even on
adversarial input. Simultaneous min/max computes your chart bounds in 1.5n comparisons.

**How:**
1. Collect the minute's latencies into an array.
2. Run QuickSelect for k = n/2 (median) and k = 0.95n (p95). Use Median-of-Medians if inputs can be
   adversarial.
3. For the min and max, process the values in pairs to save comparisons.

---

## 04 · Data Structures

### [01_stack.py](04_data_structures/01_stack.py) — Stack

**Situation:** You are validating millions of nested JSON documents in a streaming ingest job and must
reject any with unbalanced brackets.

**Why this algorithm:** A stack matches the last-opened bracket with the next closing one in O(1) per
character. That means one pass per document with no backtracking.

**How:**
1. Push each opening `{` or `[` onto the stack.
2. On each closing bracket, pop and check that it matches.
3. The document is valid if the stack is empty at the end. Otherwise send it to a dead-letter queue.

### [02_linked_list.py](04_data_structures/02_linked_list.py) — Linked List

**Situation:** A cache server keeps the most recently used keys and must constantly move items to the front
and drop items from the back, millions of times per second.

**Why this algorithm:** A linked list inserts or removes at a known node in O(1) by changing pointers,
without shifting other elements. Paired with a hash map, it forms the classic LRU cache.

**How:**
1. Keep the keys in a linked list ordered from most to least recently used.
2. Store a hash map from each key to its node, so you can find any node instantly.
3. On access, unlink the node and move it to the head. When full, remove the tail.

### [03_elementary_data_structures.py](04_data_structures/03_elementary_data_structures.py) — Linked List, Stack, Queue and Hash Table

**Situation:** You are building a mini message broker that buffers incoming events, tracks seen event IDs
for deduplication and supports undo for admin actions.

**Why this algorithm:** Each structure covers one part:
- **Queue (FIFO)**: events are processed in arrival order.
- **Hash table**: O(1) "have I seen this event ID?" checks across millions of IDs.
- **Stack (LIFO)**: undo the most recent admin action first.
- **Linked list**: cheap insertions and removals inside buffers.

**How:**
1. Enqueue incoming events. Workers dequeue them in order.
2. Before processing an event, check its ID in the hash table and skip duplicates.
3. Push each admin action onto a stack, and pop it to undo.

### [04_disjoint_set_union.py](04_data_structures/04_disjoint_set_union.py) — Disjoint-Set Union (Union-Find)

**Situation:** You have 2 billion "same person" signals (shared email, phone or device) across a customer
database and need to group the records into unique real-world people (entity resolution).

**Why this algorithm:** Union-Find merges groups and answers "same group?" in near-constant time (inverse
Ackermann) with path compression and union by rank. It processes each signal once, in any order.

**How:**
1. Make every record its own set.
2. For each signal linking records A and B, call `union(A, B)`.
3. Afterwards, `find(record)` returns a canonical person ID. Group the records by it.

### [05_trees_and_balanced_search_trees.py](04_data_structures/05_trees_and_balanced_search_trees.py) — BST and Red-Black Tree

**Situation:** A real-time trading system keeps an order book with prices constantly inserted and removed,
and needs the best bid or ask and range queries ("all orders between $100 and $105") at any moment.

**Why this algorithm:** A Red-Black Tree keeps the keys sorted and guarantees O(log n) insert, delete and
search, even under a skewed burst of inserts. A plain BST would turn into a slow linked list on sorted
input. Hash tables can't answer range queries.

**How:**
1. Insert each price level as a key in a Red-Black Tree.
2. Get the best price from the leftmost or rightmost node.
3. For range queries, walk the tree in order between the two bounds.

### [06_augmenting_data_structures.py](04_data_structures/06_augmenting_data_structures.py) — Order-Statistic Tree and Interval Tree

**Situation:** A gaming platform with 50 million players needs live leaderboard ranks ("you are #48,213").
A cloud scheduler must check whether a new job's time window overlaps reserved maintenance windows.

**Why this algorithm:**
- An **Order-Statistic Tree** stores subtree sizes, so it can find a player's rank, or the player at rank k,
  in O(log n) without re-sorting 50 million scores.
- An **Interval Tree** stores the maximum endpoint in each subtree, so it detects overlaps in O(log n)
  instead of checking every interval.

**How:**
1. Leaderboard: insert scores into the tree and update subtree sizes on each insert or rotation. Use
   `rank(score)` or `select(k)` on request.
2. Scheduler: insert reserved windows as intervals. For each new job, run an overlap query before booking.

### [07_advanced_trees_and_heaps.py](04_data_structures/07_advanced_trees_and_heaps.py) — B-Tree, Fibonacci Heap and van Emde Boas Tree

**Situation:** You are building the storage layer of an analytics database holding 10 TB on disk, plus a
route planner over a road graph with 100 million edges, plus a high-speed network switch.

**Why this algorithm:**
- **B-Tree**: each node holds hundreds of keys, so finding any row takes only 3–4 disk reads. It's the index
  in PostgreSQL, MySQL and file systems.
- **Fibonacci Heap**: O(1) amortized decrease-key makes Dijkstra faster on huge, dense graphs.
- **van Emde Boas Tree**: O(log log u) lookups over a fixed integer universe, such as IP addresses.

**How:**
1. Index the table's primary key with a B-Tree sized to the disk page (for example 8 KB nodes).
2. Use a Fibonacci heap as Dijkstra's priority queue for the road graph.
3. Use a vEB tree for next-hop lookups when keys are bounded integers.

---

## 05 · Algorithm Design Techniques

### [01_greedy_algorithms.py](05_design_techniques/01_greedy_algorithms.py) — Greedy Algorithms

**Situation:** A data lake must cut storage costs. You want to compress petabytes of logs, schedule
non-overlapping batch jobs on one shared cluster and connect data centers with minimal fiber.

**Why this algorithm:** These problems have the *greedy-choice property*: the locally best choice is part
of an optimal solution, so a single fast pass is enough.
- **Huffman coding**: the shortest codes for the most frequent symbols give optimal prefix compression.
- **Activity selection**: always running the job that finishes earliest fits the most jobs.
- **Fractional knapsack**: take the best value per unit first, for divisible resources like bandwidth.
- **Kruskal's MST**: the cheapest network linking all data centers.

**How:**
1. Count the symbol frequencies in the logs, build the Huffman tree and encode.
2. Sort the jobs by end time and pick each one that doesn't overlap the previous pick.
3. Sort the links by cost and add each one that doesn't create a cycle (checked with Union-Find).

### [02_dynamic_programming.py](05_design_techniques/02_dynamic_programming.py) — Dynamic Programming

**Situation:** A genomics pipeline compares millions of DNA reads against a reference. A cloud budget
planner chooses which indivisible jobs to run under a fixed budget. A payment network computes cheapest
routes where some fees are rebates (negative costs).

**Why this algorithm:** These problems have overlapping subproblems, which brute force would recompute
exponentially many times. DP solves each subproblem once:
- **LCS**: similarity and diffs between sequences. It's the core of `diff` and of sequence alignment.
- **0/1 Knapsack**: the best set of all-or-nothing jobs within budget, where greedy fails.
- **Bellman-Ford**: shortest paths with negative edges, plus detection of negative cycles (arbitrage).

**How:**
1. Define the subproblem, for example "LCS of the first i and j characters".
2. Fill the table bottom-up, reusing the earlier entries.
3. Read the answer from the final cell, and backtrack if you need the actual sequence or job set.

---

## 06 · Randomized Algorithms

### [01_probabilistic_and_randomized.py](06_randomized_algorithms/01_probabilistic_and_randomized.py) — Shuffle, Hiring Problem and Randomized QuickSort

**Situation:** You train a model on 500 million rows that are stored sorted by date. You also run an online
"best candidate so far" selection on a stream, and you sort user-supplied data that could be adversarial.

**Why this algorithm:**
- **Fisher-Yates** shuffles in O(n) with every ordering equally likely, so training batches aren't biased
  by date.
- The **hiring problem** shows that with random order you only "switch" about ln(n) times, which predicts
  how often an online leader changes.
- **Randomized QuickSort** picks random pivots, so no input can force the O(n²) worst case.

**How:**
1. Shuffle the row indices with Fisher-Yates before each training epoch.
2. Randomize the arrival order before streaming selection, to keep the switch count low.
3. Use random pivots when sorting untrusted input.

### [02_las_vegas_and_monte_carlo.py](06_randomized_algorithms/02_las_vegas_and_monte_carlo.py) — Las Vegas vs. Monte Carlo

**Situation:** You need exact medians over huge telemetry batches, quick estimates over data too big to
scan fully, and fast prime generation for encryption keys.

**Why this algorithm:**
- **Las Vegas (QuickSelect)**: always exact, with fast *expected* runtime. Use it when the answer must be
  correct.
- **Monte Carlo (Pi estimation)**: fixed runtime with an approximate answer. Random sampling estimates
  results over data you can't fully process.
- **Monte Carlo (Fermat test)**: very fast, and the error rate drops with each extra round.

**How:**
1. Use QuickSelect when exactness is required.
2. Use random sampling for approximate aggregates, and add samples until the error bound is acceptable.
3. Run the primality test for several rounds to make the chance of error negligible.

### [03_monte_carlo_tree_search.py](06_randomized_algorithms/03_monte_carlo_tree_search.py) — Monte Carlo Tree Search

**Situation:** A query optimizer must choose join orders for a query with 15 tables, which gives billions
of possible plans. A logistics planner chooses multi-step routing decisions under uncertainty.

**Why this algorithm:** The search space is far too large to explore fully. MCTS spends its time on the
most promising branches (exploitation) while still sampling new ones (exploration), and it can return the
best plan found so far at any time.

**How:**
1. Represent each partial plan as a tree node and each next choice as a child.
2. Repeat selection → expansion → random rollout to a full plan → backpropagate its cost.
3. When time runs out, pick the child with the most visits as the decision.

---

## 07 · Graph Algorithms

### [01_graph_fundamentals.py](07_graph_algorithms/01_graph_fundamentals.py) — BFS, DFS, Topological Sort, Dijkstra, Floyd-Warshall, SCC and Max Flow

**Situation:** You run a data platform with thousands of ETL jobs that depend on each other, and a social
graph of 100 million users.

**Why this algorithm:** Each graph question has a matching algorithm:
- **Topological sort**: run ETL jobs in an order where every input is ready first. This is how Airflow DAGs work.
- **BFS**: "people within 2 hops", the shortest path in an unweighted graph.
- **DFS**: detect cycles in job dependencies before they deadlock the scheduler.
- **Kosaraju SCC**: find tightly knit communities, or circular dependencies, in directed graphs.
- **Dijkstra / Floyd-Warshall / Edmonds-Karp**: weighted routes, all-pairs distances and capacity limits.

**How:**
1. Store the graph as an adjacency list, which scales to sparse graphs with millions of nodes.
2. Match the question to the algorithm above.
3. For graphs too big for one machine, use the same algorithms in distributed frameworks such as Spark
   GraphX or Pregel.

### [02_minimum_spanning_tree.py](07_graph_algorithms/02_minimum_spanning_tree.py) — Kruskal's MST

**Situation:** You must connect 300 edge data centers into a single replication network, and every
possible link has a different monthly cost.

**Why this algorithm:** Kruskal's algorithm guarantees the cheapest network that connects everything, in
O(E log E). It is also used for clustering: removing the most expensive MST edges splits the data into
natural clusters.

**How:**
1. List all candidate links with their costs and sort them from cheapest to most expensive.
2. Add each link unless it connects two sites that are already connected (checked with Union-Find).
3. Stop after V − 1 links. That is your minimum-cost network.

### [03_single_source_shortest.py](07_graph_algorithms/03_single_source_shortest.py) — Dijkstra's Algorithm

**Situation:** A delivery platform must compute travel times from a central warehouse to 2 million
addresses on a road network every morning.

**Why this algorithm:** With non-negative road times, Dijkstra finds the shortest path from one source to
*all* destinations in one run (O((V + E) log V) with a heap). That is far cheaper than a separate search
per address.

**How:**
1. Build the road graph with travel times as edge weights.
2. Run Dijkstra from the warehouse using a min-heap.
3. Store the resulting distance table and use it for dispatch and ETA estimates.

### [04_all_pairs_shortest.py](07_graph_algorithms/04_all_pairs_shortest.py) — Floyd-Warshall

**Situation:** An airline analytics team needs a complete table of the cheapest connections between all
400 airports they serve.

**Why this algorithm:** For a dense graph of moderate size, Floyd-Warshall computes every pair in O(V³),
about 64 million steps for 400 airports. The code is short and handles negative edges. For millions of
nodes you would run Dijkstra from each source instead.

**How:**
1. Start a V×V matrix with the direct flight costs, or ∞ where there's no direct flight.
2. For each airport k, check whether routing i → k → j beats the current i → j cost.
3. The final matrix is your all-pairs fare table.

### [05_maximum_flow.py](07_graph_algorithms/05_maximum_flow.py) — Edmonds-Karp Maximum Flow

**Situation:** A video streaming company must know how many Gbps it can push from its origin servers to a
region through a mesh of links with limited capacity. It also needs to match 10,000 jobs to workers.

**Why this algorithm:** Max flow finds the true throughput limit and the bottleneck links (the min cut),
in polynomial time. Matching jobs to workers is the same problem in disguise.

**How:**
1. Model the links as edges whose capacity is their bandwidth. Add a source and a sink.
2. Repeatedly find a shortest augmenting path with BFS and push flow along it.
3. When no path remains, the total flow is the maximum, and the saturated edges show where to upgrade.

---

## 08 · Strings and Geometry

### [01_kmp_string_matching.py](08_strings_and_geometry/01_kmp_string_matching.py) — Knuth-Morris-Pratt

**Situation:** A security team scans 50 TB of network packet captures for known attack signatures. A
genomics lab searches for a gene sequence across billions of DNA bases.

**Why this algorithm:** KMP runs in O(n + m) and never re-reads a character of the text. That suits data
streamed once from disk or the network, and it avoids the worst case of naive search on repetitive data
like DNA.

**How:**
1. Precompute the pattern's failure table: the longest prefix that is also a suffix.
2. Stream the text, and on a mismatch use the table to shift the pattern without moving backward.
3. Report each match position. For many patterns at once, extend the idea to Aho-Corasick.

### [02_convex_hull_graham.py](08_strings_and_geometry/02_convex_hull_graham.py) — Graham Scan Convex Hull

**Situation:** A ride-sharing company has 20 million GPS pickup points per city and wants a service-area
boundary. A self-driving car turns LiDAR point clouds into obstacle outlines.

**Why this algorithm:** Graham Scan finds the outer boundary in O(n log n), and the hull is usually tiny
compared with n. It turns millions of points into a polygon of a few dozen vertices that is cheap to store
and test against.

**How:**
1. Pick the lowest point, then sort the other points by their angle around it.
2. Walk through them, popping any point that makes a clockwise (inward) turn.
3. The remaining stack is the hull. Store it as the geofence polygon.

---

## 09 · Algebra and Cryptography

### [01_rsa_number_theory.py](09_algebra_and_cryptography/01_rsa_number_theory.py) — Number Theory and Mini-RSA

**Situation:** A data platform must securely exchange encryption keys with thousands of partner systems
over the public internet before transferring sensitive datasets.

**Why this algorithm:** RSA lets partners encrypt with a public key that only you can decrypt. Its security
rests on how hard it is to factor large numbers. Fast modular exponentiation, GCD and primality testing
make it practical.

**How:**
1. Generate two large primes with probabilistic primality testing, and derive the public and private keys.
2. Partners encrypt a random symmetric key with your public key.
3. You decrypt it, and both sides switch to fast symmetric encryption (like AES) for the bulk data.

### [02_fast_fourier_transform.py](09_algebra_and_cryptography/02_fast_fourier_transform.py) — Fast Fourier Transform

**Situation:** An IoT platform analyzes vibration signals from 100,000 industrial sensors, sampled
thousands of times per second, to detect failing machines.

**Why this algorithm:** FFT converts a signal into its frequencies in O(n log n) instead of O(n²). Failing
bearings show up as spikes at specific frequencies. The same trick speeds up convolution and the
multiplication of huge numbers or polynomials.

**How:**
1. Split each sensor stream into windows whose length is a power of two (for example 4096 samples).
2. Run the FFT on each window to get a frequency spectrum.
3. Raise an alert when energy at known fault frequencies goes above a baseline.

---

## 10 · Concurrency and Optimization

### [01_parallel_merge_sort.py](10_concurrency_and_optimization/01_parallel_merge_sort.py) — Parallel Merge Sort

**Situation:** A nightly job sorts 200 million records on a 32-core machine, and a single-threaded sort
leaves 31 cores idle.

**Why this algorithm:** Merge sort's halves are independent, so they can be sorted on separate cores at
the same time. The final merge is the only sequential step. This is the same pattern Spark and Hadoop use
across whole clusters.

**How:**
1. Split the data into one chunk per core.
2. Sort the chunks in parallel, here with `ProcessPoolExecutor`.
3. Merge the sorted chunks in pairs, or all at once with a k-way merge.

### [02_matrix_lu_inversion.py](10_concurrency_and_optimization/02_matrix_lu_inversion.py) — LU Decomposition

**Situation:** A recommendation system repeatedly solves large systems of linear equations
(Ax = b with the same A but thousands of different b vectors) while fitting regression models.

**Why this algorithm:** LU factorizes A once in O(n³). After that, each new b costs only O(n²) using
forward and back substitution, which is far cheaper than re-solving from scratch or explicitly inverting A
each time.

**How:**
1. Factor A = LU once, with pivoting for numerical stability.
2. For each b, solve Ly = b, then Ux = y.
3. In production, use optimized libraries like NumPy or LAPACK, which use this method internally.

### [03_simplex_solver.py](10_concurrency_and_optimization/03_simplex_solver.py) — Simplex Linear Programming

**Situation:** A cloud provider must decide how many VMs of each type to place across data centers to
maximize revenue, subject to CPU, memory, power and network limits.

**Why this algorithm:** This is a linear program: a linear objective with linear constraints. Simplex
moves between the corners of the feasible region and is very fast in practice, even with thousands of
variables. It powers capacity planning, ad-budget allocation and supply chain tools.

**How:**
1. Write the objective (revenue) and each resource limit as linear equations.
2. Convert them to standard form and run the simplex pivots until no direction improves the objective.
3. Read the optimal allocation, and use the slack values to see which resources are the bottleneck.

---

## 11 · NP-Completeness and Approximation

### [01_vertex_cover_approx.py](11_np_and_approximation/01_vertex_cover_approx.py) — Vertex Cover 2-Approximation

**Situation:** A security team must place traffic monitors on switches so that every one of 5 million
network links is watched, using as few monitors as possible.

**Why this algorithm:** Finding the exact minimum is NP-complete and infeasible at this scale. The
2-approximation runs in linear time and *guarantees* at most twice the optimal number of monitors. A
provable bound like this is often more useful than an unknown "best effort".

**How:**
1. Pick any link that isn't covered yet.
2. Put monitors on *both* of its endpoints, then remove every link they cover.
3. Repeat until every link is covered.

### [02_metric_tsp_approx.py](11_np_and_approximation/02_metric_tsp_approx.py) — Metric TSP 2-Approximation

**Situation:** A logistics company plans routes for thousands of delivery trucks every morning, each
visiting 100–200 stops, with only minutes to compute all the routes.

**Why this algorithm:** The exact traveling salesperson problem is NP-hard. Because real road distances
obey the triangle inequality, this approach builds an MST and shortcuts its walk, giving a tour at most
twice the optimal length in polynomial time. In practice it's a good starting route for local improvements
like 2-opt.

**How:**
1. Build a minimum spanning tree over each truck's stops.
2. Walk the tree depth-first (preorder) and skip stops you've already visited.
3. Return to the depot. Optionally refine the route with 2-opt swaps.
