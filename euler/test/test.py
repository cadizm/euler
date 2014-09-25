#!/usr/bin/env python


from euler.math import long_multiplication


def test_long_multiplication():
    N = 1000
    for i in range(N):
        for j in range(N):
            x = str(i * j)
            y = long_multiplication(str(i), str(j))
            assert x == y


def test_is_palindrom():
    assert is_palindrome(0) == True
    assert is_palindrome(10) == False
    assert is_palindrome(11) == True
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(1221) == True
    assert is_palindrome(1231) == False
    assert is_palindrome(990009) == False
