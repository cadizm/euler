#!/usr/bin/env python

#
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?
#


def ndigits(N):
    n, i = N, 0
    while n > 0:
        n, i = n / 10, i + 1
    return i


def fibonacci(n, d):
    "Recursive, memoized implementation"
    if n < 1:
        return None
    if n < 3:
        return 1
    if n not in d:
        d[n] = fibonacci(n - 1, d) + fibonacci(n - 2, d)
    return d[n]


if __name__ == '__main__':
    d = {}
    n, i = 1, 1
    while n != 1000:
        n, i = ndigits(fibonacci(i, d)), i + 1
    print i - 1
