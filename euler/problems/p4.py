#!/usr/bin/env python

#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#


from euler.util import is_palindrome


def run():
    L = []
    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            if is_palindrome(i * j):
                L.append(i * j)
    print max(L)
