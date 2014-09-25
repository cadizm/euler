#!/usr/bin/env python

from euler.util import rotations


def eratosthenes(N):
    """http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    def next_index(j, P):
        for i, flag in P:
            if i > j and flag:
                return i
        return None
    P = [[i, True] for i in range(N + 1)]
    j = 1
    while True:
        j = next_index(j, P)
        if not j or j**2 > N:
            break
        for k in range(j**2, len(P), j):
            P[k][1] = False
    return [i for i, flag in P if flag and i > 1]


def is_prime(n):
    """http://en.wikipedia.org/wiki/Primality_test
    """
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


def prime_factors(n):
    """
    Prime factor by method of trial division.

    http://en.wikipedia.org/wiki/Trial_division
    """
    if n == 1:
        return [1]
    primes = eratosthenes(int(n**0.5))
    prime_factors = []
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def circular_primes(limit=1000000):
    P, L = {}, []
    for p in eratosthenes(limit):
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
    return L
