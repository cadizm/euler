#!/usr/bin/env python

#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
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
    print sum(eratosthenes(2000000))
