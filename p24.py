#!/usr/bin/env python

#
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
#     012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

def next_lexicographic_permutation(a):
    "Based on wikipedia algorithm: http://goo.gl/IAGcGH"

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


if __name__ == '__main__':
    a, i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1
    b, i = next_lexicographic_permutation(a), i + 1
    while a != b and i != 1000001:
        a = b
        b, i = next_lexicographic_permutation(a), i + 1
    print i - 1, a
