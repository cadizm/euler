#!/usr/bin/env python

#
# The following iterative sequence is defined for the set of positive
# integers:
#
# n => n/2 (n is even)
# n => 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
#
# 13 => 40 => 20 => 10 => 5 => 16 => 8 => 4 => 2 => 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#


from euler.math import collatz


def run():
    d = {}
    max_chain = [0, 0]
    for i in range(1000000):
        c = collatz(i, d)
        if c > max_chain[1]:
            max_chain = [i, c]
    print max_chain
