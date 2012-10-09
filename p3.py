#!/usr/bin/env python

#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
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


def p3(n):
    """
    Return largest prime factor by method of trial division

    http://en.wikipedia.org/wiki/Trial_division
    """
    if n == 1:
        return [1]
    primes = eratosthenes(int(n**0.5))
    prime_factors = []
 
    for p in primes:
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
 
    return max(prime_factors)


if __name__ == '__main__':
    print p3(600851475143)
