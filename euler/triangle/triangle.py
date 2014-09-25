#!/usr/bin/env python


class TriangleNumberGenerator():
    """http://en.wikipedia.org/wiki/Triangular_number
    """
    def __init__(self):
        self.n = 0
        self.sum = 0

    def next(self):
        self.n += 1
        self.sum += self.n
        return self.sum


def parse_triangle(P, first_line=0):
    """Parse string into array of array's of  int's
    """
    return [[int(e) for e in p.split()] for p in P.split("\n")[first_line:-1]]


def max_path(P):
    """Return max path from `top to bottom' of triangle P
    """
    if type(P) is str:
        P = parse_triangle(P)
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
    return max(P[-1])
