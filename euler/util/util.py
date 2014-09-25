#!/usr/bin/env python


def collect(i, N):
    """Collect ith digit in number n for n in list of numbers N
    """
    C = []
    for n in N:
        C.append(n[i])
    return C


def rotate(S):
    """Return one rotation of string S
    """
    return S[1:] + S[0]


def rotations(N):
    """Rotation generator
    """
    S = str(N)
    r = rotate(S)
    while r != S:
        yield r
        r = rotate(r)


def is_palindrome(N):
    S = [s for s in str(N)]
    for i in range(len(S) / 2):
        if S[i] != S[(i + 1) * -1]:
            return False
    return True


def binstr(N):
    return bin(N)[2:]
