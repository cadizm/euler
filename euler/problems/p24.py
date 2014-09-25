#!/usr/bin/env python

#
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
#     012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?


from euler.math.discrete import next_lexicographic_permutation


def run():
    a, i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1
    b, i = next_lexicographic_permutation(a), i + 1
    while a != b and i != 1000001:
        a = b
        b, i = next_lexicographic_permutation(a), i + 1
    print i - 1, a
