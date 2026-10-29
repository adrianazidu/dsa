"""
Las Vegas vs. Monte Carlo Algorithms
------------------------------------
What it does:
- Las Vegas (Randomized QuickSelect): Always gives the 100% correct answer (e.g., finding the k-th smallest element). Its runtime is random (fast on average).
- Monte Carlo Pi Estimation: Uses random dart throws inside a square to approximate Pi. Its runtime is fixed, but the result is an approximation.
- Monte Carlo Fermat Primality Test: Rapidly tests if a large number is prime using random numbers. It never says a prime is composite, but might rarely mistake a composite for a prime.

Real-World Use Cases:
- Finding medians and percentiles in large telemetry streams without sorting everything (QuickSelect).
- Valuing complex financial stock options and simulating particle physics (Monte Carlo integration).
- Rapidly generating secure prime numbers for HTTPS/SSH encryption certificates (Primality testing).
"""

import random
import math

# 1. Las Vegas: QuickSelect (Find k-th smallest element, 0-indexed)
def las_vegas_quickselect(arr: list, k: int) -> int:
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    pivots = [x for x in arr if x == pivot]
    highs = [x for x in arr if x > pivot]

    if k < len(lows):
        return las_vegas_quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return las_vegas_quickselect(highs, k - len(lows) - len(pivots))

# 2. Monte Carlo: Estimate Pi
def monte_carlo_estimate_pi(num_samples: int) -> float:
    inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        if x * x + y * y <= 1.0:
            inside_circle += 1
    return 4.0 * (inside_circle / num_samples)

# 3. Monte Carlo: Fermat Primality Test
def fermat_is_prime(n: int, iterations: int = 10) -> bool:
    if n in (2, 3):
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for _ in range(iterations):
        a = random.randint(2, n - 2)
        # Fermat's test: a^(n-1) % n must equal 1 if n is prime
        if pow(a, n - 1, n) != 1:
            return False
    return True

if __name__ == "__main__":
    data = [77, 12, 5, 99, 23, 41]
    k = 2  # Looking for 3rd smallest (index 2)
    print(f"{k}-th smallest in {data}:", las_vegas_quickselect(data, k))
    print("Monte Carlo Pi approximation (50k points):", monte_carlo_estimate_pi(50000))
    print("Is 10007 prime?", fermat_is_prime(10007))
