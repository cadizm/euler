#!/usr/bin/env python

#
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025  385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
#

def square_sum(n):
    'Return sum of the first n numbers, squared'
    N = (n * (n + 1)) / 2
    return N**2


def square_pyramid(n):
    """Return nth square pyramid number
    This is equivalent to the sum of first n square numbers"""
    N = (n * (n + 1) * ((2 * n) + 1)) / 6
    return N


if __name__ == '__main__':
    n = 100
    print 'n = {0}: {1}'.format(n, square_sum(n) - square_pyramid(n))
