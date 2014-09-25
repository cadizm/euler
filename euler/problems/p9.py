#!/usr/bin/env python

#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which,
#
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#


from euler.math import pythagorean_triplet


def run():
    print pythagorean_triplet(1000)
