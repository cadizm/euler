#!/usr/bin/env python


#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#

F = {}


def digits(N):
    n = N
    res = []
    while n > 0:
        d = n % 10
        res.insert(0, d)
        n = n / 10
    return res


def factorial(N):
    if N < 0:
        return None
    if N in [0, 1]:
        return 1
    if N in F:
        return F[N]
    F[N] = N * factorial(N - 1)
    return F[N]


def sum_factorial_digits(N):
    return sum([factorial(i) for i in digits(N)])


if __name__ == '__main__':
    L = []
    for i in range(3, 100000):
        if i == sum_factorial_digits(i):
            L.append(i)
    print sum(L)
