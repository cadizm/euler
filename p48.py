#!/usr/bin/env python

#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
#

if __name__ == '__main__':
    sum = 0
    for i in range(1, 1000 + 1):
        sum += i**i
    last_10 = ''
    for i in range(10):
        last_10 = str(sum % 10) + last_10
        sum /= 10
    print last_10
