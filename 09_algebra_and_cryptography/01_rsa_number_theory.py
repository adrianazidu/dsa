"""
ALGORITHM: Number Theory Primitives & Public-Key Cryptography (Mini-RSA)

WHAT IT DOES (SIMPLY):
How can two people who have never met send a secret message over the public internet without
an eavesdropper reading it? Public-key cryptography uses "one-way math": it is very easy to
multiply two giant prime numbers together, but almost impossible for a supercomputer to take the
result and work backwards to find the original primes. This file implements the math engine behind
it: finding common divisors, testing if giant numbers are prime, and locking/unlocking messages.

REAL-LIFE USE CASES:
- HTTPS & Web Browsing: Securing credit card entries and logins over TLS/SSL certificates.
- SSH Keys & Secure Login: Authenticating developers connecting to remote cloud servers.
- Blockchain & Cryptocurrencies: Verifying Bitcoin and Ethereum transactions with digital signatures.
- Error Correction (QR Codes): Reed-Solomon math restoring scratched or blurry QR codes.
"""

# Import random for witness generation in Miller-Rabin
import random


# Extended Euclidean Algorithm: computes gcd(a, b) and Bezout coefficients
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


# Modular multiplicative inverse: (a * x) % m == 1
def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % m + m) % m


# Fast modular exponentiation: computes (base^exp) % mod
def mod_pow(base, exp, mod):
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res


# Miller-Rabin randomized primality test
def is_prime(n, k=10):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Factor out powers of 2: n - 1 = d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = mod_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        composite = True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        if composite:
            return False

    return True


if __name__ == "__main__":
    # Mini-RSA demo
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = mod_inverse(e, phi)

    msg = 42
    cipher = mod_pow(msg, e, n)
    decrypted = mod_pow(cipher, d, n)
    print(f"Original: {msg} | Cipher: {cipher} | Decrypted: {decrypted}")
    print(f"Is 104729 prime?: {is_prime(104729)}")
