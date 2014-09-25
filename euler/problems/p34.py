#!/usr/bin/env python

#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#


from euler.math import sum_factorial_digits


def run():
    L = []
    for i in range(3, 100000):
        if i == sum_factorial_digits(i):
            L.append(i)
    print sum(L)
