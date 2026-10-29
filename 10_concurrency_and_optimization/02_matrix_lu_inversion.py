"""
ALGORITHM: Matrix Operations & Inversion via LU Decomposition

WHAT IT DOES (SIMPLY):
A matrix is a grid of numbers representing a transformation or a big system of equations
(e.g., balancing 50 variables at once). Inverting a matrix is like finding the "undo" button
for that transformation. Doing it naively is incredibly slow, so we split the matrix into
a Lower triangular and an Upper triangular piece (LU decomposition), which turns a messy
equation system into a step-by-step puzzle that solves in seconds.

REAL-LIFE USE CASES:
- Machine Learning & Deep Learning: Training neural networks (GEMM matrix multiplications).
- 3D Computer Graphics & Animation: Rotating, zooming, and positioning 3D objects on screen.
- Robotics & Self-Driving Cars: Kalman filters estimating exact car position from noisy GPS/sensors.
- Structural Engineering: Simulating stress and load on bridges and skyscrapers.
"""

# Matrix multiplication of two 2D lists (A: m x k, B: k x n)
def matrix_multiply(A, B):
    r_A, c_A, c_B = len(A), len(A[0]), len(B[0])
    C = [[0.0] * c_B for _ in range(r_A)]
    for i in range(r_A):
        for j in range(c_B):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(c_A))
    return C


# LU Decomposition of an N x N matrix without pivoting
def lu_decomposition(A):
    n = len(A)
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    U = [[float(val) for val in row] for row in A]

    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]

    return L, U


# Forward substitution: solves L * y = b
def forward_substitution(L, b):
    y = [0.0] * len(b)
    for i in range(len(b)):
        known_sum = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b[i] - known_sum
    return y


# Backward substitution: solves U * x = y
def backward_substitution(U, y):
    n = len(y)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        known_sum = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - known_sum) / U[i][i]
    return x


# Inverts matrix A by solving columns against identity vectors
def matrix_inverse(A):
    n = len(A)
    L, U = lu_decomposition(A)
    inv_cols = []

    for col_idx in range(n):
        e = [1.0 if r == col_idx else 0.0 for r in range(n)]
        y = forward_substitution(L, e)
        x = backward_substitution(U, y)
        inv_cols.append(x)

    # Transpose column vectors into row-major matrix
    return [[inv_cols[col][row] for col in range(n)] for row in range(n)]


if __name__ == "__main__":
    A = [[4.0, 7.0, 2.0], [3.0, 6.0, 1.0], [2.0, 5.0, 3.0]]
    inv_A = matrix_inverse(A)
    print("Inverted Matrix:")
    for row in inv_A:
        print([round(v, 4) for v in row])
