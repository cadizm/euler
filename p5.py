#!/usr/bin/env python

#
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible (divisible with
# no remainder) by all of the numbers from 1 to 20?
#

def gcd(a, b):
    "Euclid's algorithm"
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    "Reduction by gcd"
    return (a * b) / gcd(a, b)


def p5():
    R = range(1, 20 + 1)
    n = 1
    for i in R:
        n = lcm(i, n)
    return n


if __name__ == '__main__':
    print p5()
