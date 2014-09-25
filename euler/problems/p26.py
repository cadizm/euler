#!/usr/bin/env python

#
# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
# be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.
#
# ===========================================================================
#
# http://mathforum.org/library/drmath/view/58073.html
#
# Fractions with Repeating Decimals
#
# Date: 02/24/97 at 14:08:30
# From: Anonymous
# Subject: Fractions with Repeating Decimals
#
# How do you know if a fraction will have a repeating decimal or if it
# will terminate?
#
# Thanks!
#
# Date: 03/14/97 at 11:45:59
# From: Doctor Bill
# Subject: Re: Fractions with Repeating Decimals
#
# Dear Cameron,
#
# The answer is not too obvious.
#
# First, put the fraction in lowest terms.  Now look at the denominator.
# If the only prime factors of the denominator are 2's and 5's, then the
# decimal expansion of the fraction will terminate.  Otherwise, it will
# repeat.  Another way to say this condition is that the denominator
# (when the fraction is in lowest terms) can be written of the form
# (2^n)*(5^m), where n and m are integers greater than or equal to zero
# (the ^ means exponent).
#
# Why is this true?  It has to do with the fact that our number system
# is in base 10 and the only factors to 10 are 5 and 2.  If you take any
# terminating fraction, like 4.25, you can multiply it by a power of 10
# to get an integer.  This is illustrated in the following equation (p/q
# is the fraction representation for 4.25 in lowest terms):
#
# 4.25 = 100 * p/q  =  an integer.
#
# Thus the 100 must have cancelled out q, and therefore the only factors
# of q were 2's and 5's.
#
# We hope this helps,
#
# -Doctors Bill and Ken,  The Math Forum
#  Check out our web site!  http://mathforum.org/dr.math/
#
#
# ===========================================================================
#
# http://en.wikipedia.org/wiki/Repeating_decimal
#
# Decimal expansion and recurrence sequence
# In order to convert a rational number represented as a fraction into decimal
# form, one may use long division. For example, consider the rational number
# 5/74:
#
#         0.0675
#       --------
#    74 )5.00000
#        4.44
#        ----
#          560
#          518
#          ---
#           420
#           370
#           ---
#            500
#
# etc. Observe that at each step we have a remainder; the successive remainders
# displayed above are 56, 42, 50. When we arrive at 50 as the remainder, and
# bring down the "0", we find ourselves dividing 500 by 74, which is the same
# problem we began with. Therefore the decimal repeats: 0.0675 675 675 ...
#


from euler.math import long_division
import re


def run():
    d, max_cycle = None, ''
    for i in range(2, 1000):
        res = long_division(1, i)
        m = re.match(r'^.*\((?P<cycle>.*?)\).*?$', res)
        if m:
            cycle = m.group('cycle')
            if len(cycle) > len(max_cycle):
                max_cycle = cycle
                d = i
    print d, max_cycle
