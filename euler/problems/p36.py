#!/usr/bin/env python

#
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)
#


from euler.util import is_palindrome, binstr


def run():
    N = 0
    for i in range(1000000):
        if is_palindrome(i) and is_palindrome(binstr(i)):
            N += i
    print N
