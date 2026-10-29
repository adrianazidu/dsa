"""
ALGORITHM: Linear Programming (Dantzig's Simplex Algorithm)

WHAT IT DOES (SIMPLY):
Imagine you run a factory making chairs and tables. You want to make the absolute maximum
profit, but you are limited by wood supply, labor hours, and warehouse space.
All these rules form a multi-sided shape of valid production choices. The Simplex algorithm
starts at zero and "walks" along the outer corners of that shape, always moving toward higher
profit until no adjacent corner offers more money.

REAL-LIFE USE CASES:
- Oil Refinery Production: Deciding how many barrels of crude to blend into gasoline vs. jet fuel.
- Airline Fleet Assignment: Choosing which airplanes fly which routes to minimize fuel and labor costs.
- Investment Portfolio Optimization: Balancing stock weights to maximize yield under risk caps.
- Food & Diet Formulation: Computing the cheapest animal feed mix that still satisfies all nutritional requirements.
"""

# Simplex Maximization solver: Maximize c^T * x subject to A * x <= b and x >= 0
def simplex_maximize(c, A, b):
    m = len(A)  # Number of constraints
    n = len(c)  # Number of decision variables

    # Allocate tableau: (m + 1) rows by (n + m + 1) columns
    tableau = [[0.0] * (n + m + 1) for _ in range(m + 1)]

    # Fill constraint entries and slack variables
    for i in range(m):
        for j in range(n):
            tableau[i][j] = float(A[i][j])
        tableau[i][n + i] = 1.0
        tableau[i][-1] = float(b[i])

    # Fill objective row
    for j in range(n):
        tableau[m][j] = -float(c[j])

    # Initial basis contains slack variables
    basis = [n + i for i in range(m)]

    while True:
        min_val = min(tableau[m][:-1])
        # Optimal condition reached
        if min_val >= 0:
            break

        pivot_col = tableau[m][:-1].index(min_val)

        # Minimum Ratio Test
        ratios = []
        for i in range(m):
            if tableau[i][pivot_col] > 1e-9:
                ratios.append((tableau[i][-1] / tableau[i][pivot_col], i))
            else:
                ratios.append((float("inf"), i))

        min_ratio, pivot_row = min(ratios, key=lambda x: x[0])
        if min_ratio == float("inf"):
            raise ValueError("Linear Program is unbounded")

        # Pivot step: normalize pivot row
        pivot_elem = tableau[pivot_row][pivot_col]
        tableau[pivot_row] = [v / pivot_elem for v in tableau[pivot_row]]

        # Eliminate pivot column in remaining rows
        for i in range(m + 1):
            if i != pivot_row:
                mult = tableau[i][pivot_col]
                tableau[i] = [
                    val - mult * p_val
                    for val, p_val in zip(tableau[i], tableau[pivot_row])
                ]

        basis[pivot_row] = pivot_col

    # Extract final decision variable assignments
    solution = [0.0] * n
    for i in range(m):
        if basis[i] < n:
            solution[basis[i]] = tableau[i][-1]

    optimal_val = tableau[m][-1]
    return solution, optimal_val


if __name__ == "__main__":
    c_vec = [3.0, 5.0]
    A_mat = [[1.0, 0.0], [0.0, 2.0], [3.0, 2.0]]
    b_vec = [4.0, 12.0, 18.0]
    sol, opt = simplex_maximize(c_vec, A_mat, b_vec)
    print(f"Optimal Solution [x1, x2]: {sol}")
    print(f"Max Value: {opt}")
