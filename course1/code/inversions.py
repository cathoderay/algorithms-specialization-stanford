"""
    Author: Ronald Andreu Kaiser
    Last update: January 3rd, 2024

    Algorithm specialization by Stanford (via Coursera)
    Course: Divide and Conquer, Sorting and Searching, and Randomized Algorithms 
    Module: 2

    Note: Implementation reviewed after course finished
"""


def merge_and_count_split(b, c):
    i = j = k = 0
    inversions = 0
    d = []
    while k < (len(b) + len(c)):
        if i < len(b) and j < len(c):
            if b[i] <= c[j]:
                d.append(b[i])
                i += 1
            else:
                inversions += (len(b) - i)
                d.append(c[j])
                j += 1
        else:
            if i >= len(b):
                d.append(c[j])
                j += 1
            else:
                d.append(b[i])
                i += 1
        k += 1
    return d, inversions


def sort_and_count(a):
    n = len(a)
    if n == 1: return a, 0

    b, x = sort_and_count(a[:(n//2)])
    c, y = sort_and_count(a[(n//2):])
    d, z = merge_and_count_split(b, c)

    return d, x + y + z


if __name__ == "__main__":
    a = [int(input()) for _ in range(100_000)]
    print(sort_and_count(a)[1])
