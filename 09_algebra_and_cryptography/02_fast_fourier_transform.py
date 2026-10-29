"""
ALGORITHM: Fast Fourier Transform (FFT) & Polynomial Multiplication

WHAT IT DOES (SIMPLY):
Think of sound: you hear a complex chord, but your brain can pick out the piano note from
the guitar note. The FFT acts like an optical prism for data: it splits a complicated signal
over time into its individual frequency ingredients. In math, it also allows us to multiply
two massive polynomials (or giant numbers with millions of digits) blindingly fast by temporarily
converting them into frequency points, multiplying them simply, and converting them back.

REAL-LIFE USE CASES:
- Audio Processing & Equalizers: Noise-cancelling headphones and Spotify sound equalizers.
- Medical Scanners (MRI / CT): Reconstructing sharp bodily images from raw radio frequency signals.
- Telecommunications (5G & Wi-Fi): OFDM technology splitting wireless signals across frequencies.
- Big-Number Arithmetic: Multiplying million-digit numbers in cryptography libraries.
"""

# Import cmath for native complex arithmetic
import cmath


# Recursive Cooley-Tukey Radix-2 FFT
def fft(a, invert=False):
    n = len(a)
    if n <= 1:
        return a

    # Divide step into even and odd indices
    even = fft(a[0::2], invert)
    odd = fft(a[1::2], invert)

    # Calculate angle for the roots of unity
    angle = 2 * cmath.pi / n * (-1 if invert else 1)
    w_step = cmath.rect(1.0, angle)
    w = 1.0 + 0.0j

    combined = [0.0 + 0.0j] * n
    for k in range(n // 2):
        combined[k] = even[k] + w * odd[k]
        combined[k + n // 2] = even[k] - w * odd[k]
        w *= w_step

    if invert:
        combined = [val / 2 for val in combined]

    return combined


# Polynomial multiplication in O(N log N) using FFT
def multiply_polynomials(poly_a, poly_b):
    needed_len = len(poly_a) + len(poly_b) - 1
    n = 1
    while n < needed_len:
        n <<= 1

    # Zero-pad inputs to nearest power of 2
    padded_a = poly_a + [0] * (n - len(poly_a))
    padded_b = poly_b + [0] * (n - len(poly_b))

    # Forward FFT evaluations
    vals_a = fft(padded_a, invert=False)
    vals_b = fft(padded_b, invert=False)

    # Pointwise multiplication
    vals_c = [va * vb for va, vb in zip(vals_a, vals_b)]

    # Inverse FFT back to coefficients
    raw_coeffs = fft(vals_c, invert=True)
    return [round(c.real) for c in raw_coeffs[:needed_len]]


if __name__ == "__main__":
    p1 = [1, 2, 3]  # 1 + 2x + 3x^2
    p2 = [4, 5, 6]  # 4 + 5x + 6x^2
    res = multiply_polynomials(p1, p2)
    print(f"Product Coefficients: {res}")
