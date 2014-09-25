#!/usr/bin/env python

#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10,001st prime number?
#


from euler.math.primes import eratosthenes


def run():
    key = 10001
    i = 1
    P = eratosthenes(key * i)
    while len(P) < key:
        i *= 2
        P = eratosthenes(key * i)
    print P[key - 1]
