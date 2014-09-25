#!/usr/bin/env python

#
# An irrational decimal fraction is created by concatenating the positive
# integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the
# following expression.
#
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
#


from euler.math import champernowne_constant


def run():
    e = [1, 10, 100, 1000, 10000, 100000, 1000000]
    print champernowne_constant(e)
