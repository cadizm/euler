#!/usr/bin/env python

#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?
#

def eratosthenes(n):
    'http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes'
    def next_index(j, P):
        for i, flag in P:
            if i > j and flag:
                return i
        return None
    P = [[i, True] for i in range(n + 1)]
    j = 1
    while True:
        j = next_index(j, P)
        if j**2 > n:
            break
        for k in range(j**2, len(P), j):
            P[k][1] = False
    return [i for i, flag in P if flag and i > 1]


if __name__ == '__main__':
    key = 10001
    i = 1
    P = eratosthenes(key * i)
    while len(P) < key:
        i *= 2
        P = eratosthenes(key * i)
    print P[key - 1]
