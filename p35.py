#!/usr/bin/env python

#
# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 
# 73, 79, and 97.
#
# How many circular primes are there below one million?
#

from euler import eratosthenes


def rotate(S):
    "return one rotation of string S"
    return S[1:] + S[0]


def rotations(N):
    S = str(N)
    r = rotate(S)
    while r != S:
        yield r
        r = rotate(r)


def is_prime(n):
    "http://en.wikipedia.org/wiki/Primality_test"
    n = int(n)
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_divisor = int(n**0.5)
    divisor = 5
    while divisor <= max_divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


if __name__ == '__main__':
    P, L = {}, []
    for p in eratosthenes.sieve(1000000):
        P[p] = 1
    for p in P.keys():
        flag = True
        for r in rotations(p):
            if r not in P:
                if is_prime(r):
                    P[r] = 1
                else:
                    flag = False
                    break
        if flag:
            L.append(p)
    print len(L)
