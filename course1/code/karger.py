"""
    Author: Ronald Andreu Kaiser
    Date: Jan 1st, 2025

    Algorithm specialization by Stanford (via Coursera)
    Course: Divide and Conquer, Sorting and Searching, and Randomized Algorithms 
    Module: 4
"""


from random import choice
from copy import deepcopy 


def karger(V, E):

    while len(V) > 2:
        # pick a random edge
        u = v = 1
        while not (u != v and v in E[u]): 
            v = choice(V)
            u = choice(V)
        if v < u: v, u = u, v

        # put all edges from v into u's list
        for w in E[v]: 
            if w in E: 
                E[w].remove(v)
                E[w].append(u)
            E[u].append(w)
        
        # remove v from list of vertices
        V.remove(v)
        
        # remove v's list of adjacency
        del E[v]

        # remove self-loops 
        if u in E[u]:
            E[u].remove(u)

    u, v = E.keys()
    x = E[u].count(v)
    y = E[v].count(u)
    assert x == y
    return x

        
def find_min_cut(V, E):
    return min(karger(deepcopy(V), deepcopy(E)) for _ in range(200))


if __name__ == "__main__":
    V = list(range(1, 201))
    E = {}
    for i in range(200):
        E[i+1] = list(map(int, input().split()[1:]))

    print(find_min_cut(V, E))