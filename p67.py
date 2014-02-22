#!/usr/bin/env python

#
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'), a 15K text file containing a triangle with
# one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not possible
# to try every route to solve this problem, as there are 299 altogether! If you
# could check one trillion (1012) routes every second it would take over twenty
# billion years to check them all. There is an efficient algorithm to solve it.
# ;o)
#

P = open('data/triangle.txt', 'r').read()

def parse_puzzle(P):
    "parse string into array of array's of  int's"
    return [[int(e) for e in p.split()] for p in P.split("\n")[:-1]]


if __name__ == '__main__':
    P = parse_puzzle(P)
    for i, L in enumerate(P):
        if i == 0:
            continue
        for j, e in enumerate(L):
            if j == 0:
                P[i][j] = e + P[i - 1][j]
            elif j == len(L) - 1:
                P[i][j] = e + P[i - 1][j - 1]
            else:
                P[i][j] = e + max(P[i - 1][j - 1], P[i - 1][j])
    print max(P[-1])
