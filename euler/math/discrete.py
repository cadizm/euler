#!/usr/bin/env python


def next_lexicographic_permutation(a):
    """Based on wikipedia algorithm: http://goo.gl/IAGcGH
    """
    # Don't modify the passed list
    a = list(a)
    # Find the *largest* index k such that a[k] < a[k + 1]
    k = len(a) - 2
    flag = False
    while k >= 0:
        if a[k] < a[k + 1]:
            flag = True
            break
        k = k - 1
    # If no such index exists, the permutation is the last permutation
    if not flag:
        return a
    # Find the largest index l such that a[k] < a[l]
    l = len(a) - 1
    while l >= 0:
        if a[k] < a[l] and k != l:
            break
        l = l - 1
    # Swap the value of a[k] with that of a[l]
    temp = a[k]
    a[k] = a[l]
    a[l] = temp
    # Reverse the sequence from a[k + 1] up to and including the final
    # element a[n]
    return a[:k + 1] + list(reversed(a[k + 1:]))
