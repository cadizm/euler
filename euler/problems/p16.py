#!/usr/bin/env python

#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#


from euler.math import long_multiplication


def run():
    L = ['2' for i in range(1000)]
    M = [int(e) for e in reduce(long_multiplication, L)]
    print sum(M)
