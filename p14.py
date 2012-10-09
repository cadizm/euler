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

def collatz(n, d={}):
    """http://en.wikipedia.org/wiki/Collatz_conjecture
    Implementation note: memoize results into dict d"""
    if n in d:
        return d[n]
    N, i = n, 0
    while N > 1:
        if N in d:
            d[n] = d[N] + i
            return d[n]
        i += 1
        if N % 2 == 0:
            N /= 2
        else:
            N = 3 * N + 1
    d[n] = i + 1
    return i + 1

if __name__ == '__main__':
    d = {}
    max_chain = [0, 0]
    for i in range(1000000):
        c = collatz(i, d)
        if c > max_chain[1]:
            max_chain = [i, c]
    print max_chain
