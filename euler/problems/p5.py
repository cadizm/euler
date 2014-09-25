#!/usr/bin/env python

#
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible (divisible with
# no remainder) by all of the numbers from 1 to 20?
#


from euler.math import smallest_multiple


def run():
    print smallest_multiple(1, 20 + 1)
