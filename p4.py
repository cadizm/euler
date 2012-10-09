#!/usr/bin/env python

#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#

def is_palindrome(n):
    'return True if palindrome, False otherwise'
    N = str(n)
    length = len(N)
    if length == 1:
        return True
    elif length == 2:
        if N[0] == N[1]:
            return True
        else:
            return False
    else:
        first, last = 0, length - 1
        if length % 2 == 0:  # even
            while first < last:
                if N[first] != N[last]:
                    return False
                first += 1
                last -= 1
        else:  # odd
            while first != last:
                if N[first] != N[last]:
                    return False
                first += 1
                last -= 1
    return True


def p4():
    'Brute force method'
    L = []
    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            if is_palindrome(i * j):
                L.append(i * j)
    return max(L)


if __name__ == '__main__':
#    print '0 ', is_palindrome(0)
#    print '10 ', is_palindrome(10)
#    print '11 ', is_palindrome(11)
#    print '121 ', is_palindrome(121)
#    print '123 ', is_palindrome(123)
#    print '1221', is_palindrome(1221)
#    print '1231 ', is_palindrome(1231)
#    print '990009 ', is_palindrome(990009)
    print p4()
