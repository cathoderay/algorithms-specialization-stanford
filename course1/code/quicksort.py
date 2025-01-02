"""
    Author: Ronald Andreu Kaiser
    Date: December 29th, 2024

    Algorithm specialization by Stanford (via Coursera)
    Course: Divide and Conquer, Sorting and Searching, and Randomized Algorithms 
    Module: 3
"""

from copy import copy



def pick_pivot(l, s, e):
    if STRATEGY == 'first':
        pass
    elif STRATEGY == 'last':
        l[s], l[e] = l[e], l[s]
    elif STRATEGY == "median-of-three":
        x = l[s]
        y = l[(s + e) // 2]
        z = l[e]
        if (x < y < z) or (z < y < x):
            l[s], l[(s + e) // 2] = l[(s + e) // 2], l[s] 
        elif (x < z < y) or (y < z < x):
            l[s], l[e] = l[e], l[s]
    return l[s]


def partition(l, s, e):
    p = pick_pivot(l, s, e)
    i = j = s + 1
    for j in range(s + 1, e + 1):
        if l[j] < p:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[s], l[i-1] = l[i-1], l[s]
    return i - 1


def quicksort(l, s, e):
    global comparisons

    if e <= s: return 

    comparisons += e - s

    p = partition(l, s, e)
    quicksort(l, s, p - 1)
    quicksort(l, p + 1, e)


if __name__ == "__main__":
    a = [int(input()) for _ in range(10000)]
   
    comparisons = 0
    b = copy(a)
    STRATEGY = "first"
    quicksort(b, 0, 9999)
    print(comparisons)
    assert list(sorted(b)) == b
    assert list(sorted(a)) != a

    comparisons = 0
    c = copy(a) 
    STRATEGY = "last"
    quicksort(c, 0, 9999)
    print(comparisons)
    assert list(sorted(c)) == c
    assert list(sorted(a)) != a

    comparisons = 0
    d = copy(a)
    STRATEGY = "median-of-three"
    quicksort(d, 0, 9999)
    print(comparisons)
    assert list(sorted(d)) == d
    assert list(sorted(a)) != a
