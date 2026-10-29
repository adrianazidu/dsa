"""
Master Theorem Solver
=====================

What It Does:
-------------
A helper tool that tells you how fast a recursive algorithm runs without having to do manual math.
Simply put:
Whenever an algorithm splits a problem into smaller identical pieces:
- It checks how many pieces are created (a).
- It checks how much smaller each piece is (b).
- It checks how much extra work is done combining them (d).
Then, it tells you who wins:
- The subproblems (leaves do most work).
- The combine step (top level does most work).
- Or a tie (work is evenly balanced at every level).

Use Cases:
----------
- Algorithm design: quickly verifying if a new recursive idea will be fast enough before writing it.
- Computer science coursework and exam verification.
- Performance auditing of divide-and-conquer systems (e.g. comparing Strassen vs standard matrix multiply).
"""

import math


def solve_master_theorem(a: int, b: int, d: float) -> str:
    """
    Solves recurrences of the form:
    T(n) = a * T(n/b) + O(n^d)
    
    a: number of recursive calls
    b: factor by which input size shrinks
    d: power of n for non-recursive combine work
    """
    critical_exponent = math.log(a, b)
    tolerance = 1e-6

    # Case 2: Balance between branching and combining
    if abs(critical_exponent - d) < tolerance:
        if d == 0:
            return "Theta(log(n))"
        return f"Theta(n^{d:.2f} * log(n))"

    # Case 1: Subproblems (leaves) dominate
    elif critical_exponent > d:
        return f"Theta(n^{critical_exponent:.2f})"

    # Case 3: Combining work (root) dominates
    else:
        return f"Theta(n^{d:.2f})"


if __name__ == "__main__":
    examples = [
        ("Merge Sort", 2, 2, 1),
        ("Binary Search", 1, 2, 0),
        ("Strassen Matrix Multiplication", 7, 2, 2),
        ("Karatsuba Integer Multiplication", 3, 2, 1),
    ]

    print("Master Theorem Complexity Results:")
    print("-" * 50)
    for name, a, b, d in examples:
        complexity = solve_master_theorem(a, b, d)
        print(f"{name:35s} -> {complexity}")
