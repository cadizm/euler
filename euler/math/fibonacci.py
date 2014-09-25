#!/usr/bin/env python


def even_fibonacci(limit=4000000):
    N = [1, 2]
    while True:
        if N[-1] + N[-2] > 4000000:
            break
        N.append(N[-1] + N[-2])
    return sum([n for n in N if n % 2 == 0])


def fibonacci(n, d):
    "Recursive, memoized implementation"
    if n < 1:
        return None
    if n < 3:
        return 1
    if n not in d:
        d[n] = fibonacci(n - 1, d) + fibonacci(n - 2, d)
    return d[n]
