"""
Dynamic Programming (DP)
------------------------
What it does:
Solves complex problems by breaking them into smaller subproblems, solving each subproblem once, and saving the answer in a table so it never has to be recalculated.
- 0/1 Knapsack: Packs items with given weights and values to maximize total value without exceeding a weight limit.
- Longest Common Subsequence (LCS): Finds the longest chain of characters that appear in the exact same relative order inside two texts.
- Bellman-Ford Shortest Path: Computes the shortest travel path on a network, even when some paths have negative costs.

Real-World Use Cases:
- `git diff` and file comparison tools (using LCS to show lines added/removed).
- DNA and RNA sequencing: finding similarities between genetic strands.
- Capital budgeting and resource planning (Knapsack).
- Financial currency arbitrage: finding cycles of currency exchanges that yield profit (Bellman-Ford).
"""

# 1. 0/1 Knapsack
def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w, v = weights[i - 1], values[i - 1]
        for cap in range(capacity + 1):
            if w > cap:
                dp[i][cap] = dp[i - 1][cap]
            else:
                dp[i][cap] = max(dp[i - 1][cap], dp[i - 1][cap - w] + v)
    return dp[n][capacity]

# 2. Longest Common Subsequence (LCS)
def longest_common_subsequence(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)
    dp = [[""] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    return dp[m][n]

if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 8]
    cap = 5
    print(f"Knapsack max value (cap={cap}):", knapsack_01(weights, values, cap))
    str1, str2 = "HUMAN", "CHIMPANZEE"
    print(f"LCS between '{str1}' and '{str2}':", longest_common_subsequence(str1, str2))
