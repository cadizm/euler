#!/usr/bin/env python

#
# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.
#
# ===========================================================================
#
# from http://www.mathblog.dk/project-euler-30-sum-numbers-that-can-be-written-as-the-sum-fifth-powers-digits/
# I definitely want to pursue a brute force strategy in C#, but we need an
# upper bound if we don't want to continue in eternity. So finding the upper
# bound is the secret to solving this problem. The rest is straight forward.
#
# So lets determine the upper bound. We need to find a number x * 9^5 which
# gives us an x digit number. We can do this by hand. Since 9^5 = 59049, we
# need at least 5 digits. 5 *9^5 = 295245, so with 5 digits we can make a 6
# digit number.  6 * 9^5 = 354294. So 355000 seems like a reasonable upper
# bound to use. We could probably tighten is even further if we wanted.
#

#
# http://mathworld.wolfram.com/NarcissisticNumber.html
# An n-digit number that is the sum of the nth powers of its digits is called
# an n-narcissistic number.
#


from euler.math import narcissistic_upper
from euler.math import nth_power_digit_sum


def run():
    N = 5
    L = []
    for i in range(2, narcissistic_upper(N)):
        if i == nth_power_digit_sum(5, i):
            L.append(i)
    print sum(L)
