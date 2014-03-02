#!/usr/bin/env python

def sieve(N):
    'http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes'
    def next_index(j, P):
        for i, flag in P:
            if i > j and flag:
                return i
        return None
    P = [[i, True] for i in range(N + 1)]
    j = 1
    while True:
        j = next_index(j, P)
        if j**2 > N:
            break
        for k in range(j**2, len(P), j):
            P[k][1] = False
    return [i for i, flag in P if flag and i > 1]
