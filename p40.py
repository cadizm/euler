#!/usr/bin/env python

#
# An irrational decimal fraction is created by concatenating the positive 
# integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the 
# following expression.
#
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
#


def ndigits(N):
    n, i, L = N, 1, []
    while n >= 10:
        L.append(n % 10)
        n /= 10
        i += 1
    return i, [n] + L


if __name__ == '__main__':
    E = [1, 10, 100, 1000, 10000, 100000, 1000000]
    n, res = 0, 1
    for i in range(E[-1] + 1):
        m, L = ndigits(i)
        M = range(n, n + len(L))
        for j, k in enumerate(M):
            if k in E:
                res *= L[j]
        n += m
    print res
