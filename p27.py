#!/usr/bin/env python

#
# Euler discovered the remarkable quadratic formula:
#
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is
# divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
# divisible by 41.
#
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
# primes for the consecutive values n = 0 to 79. The product of the
# coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#
# n^2 + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.
#

from euler import primes


Q = {}

def quadratic(n, a, b):
    k = (n, a, b)
    if k in Q:
        return Q[k]
    Q[k] = (n * n) + (a * n) + b
    return Q[k]


def quadratic_range(N, A, B):
    coeff_a, coeff_b, nprimes = None, None, 0
    for a in range(-A, A):
        for b in range(-B, B):
            for n in range(N):
                q = quadratic(n, a, b)
                if not primes.is_prime(q):
                    break
                elif n > nprimes:
                    coeff_a, coeff_b, nprimes = a, b, n + 1
    return coeff_a, coeff_b, nprimes


if __name__ == '__main__':
    a, b, nprimes = quadratic_range(100, 1000, 1000)
    print a * b
