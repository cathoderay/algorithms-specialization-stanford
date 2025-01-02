"""
    Author: Ronald Andreu Kaiser
    Date: December 27th, 2024

    Algorithm specialization by Stanford (via Coursera)
    Course: Divide and Conquer, Sorting and Searching, and Randomized Algorithms 
    Module: 1

    Karatsuba algorithm idea:
        x * y => (10^(n/2)*a + b) * (10^(n/2)*c + d)
        x * y => 10^n*(ac) + 10^(n/2)*(ad + bc) + bd
        step 1 => recursively compute ac
        step 2 => recursively compute bd
        step 3 => recursively compute (a + b)*(c + d) = ac + ad + bc + bd
        Gauss's trick => step 3 - step 2 - step 1 => ad + bc
"""


def split(r, n):
    x = str(r).zfill(n)
    return (int(x[:n//2]), int(x[n//2:]))


def calculate_n(x, y):
    n = max(len(str(x)), len(str(y)))
    k = 1 
    while k < n:
        k <<= 1
    return k


def multiply(x, y):
    n = calculate_n(x, y)

    if n <= 1: return x * y

    a, b = split(x, n)
    c, d = split(y, n)

    w = multiply(a, c)
    k = multiply(b, d)
    t = multiply(a + b, c + d) - w - k
    
    return w * (10**n) + t * (10**(n//2)) + k


if __name__ == "__main__":
    assert split(12, 4) == (0, 12)
    assert split(1234, 4) == (12, 34)

    assert multiply(12, 5678) == 12 * 5678
    assert multiply(12, 134) == 12 * 134
    assert multiply(7, 134) == 7 * 134

    assert multiply(1234, 5678) == 7006652
