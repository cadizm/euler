#!/usr/bin/env python

#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#

# TODO: I'm really ugly, please fix me
def long_multiply(X, Y):
    """Long multiplication of X and Y
    Result returned as str. Params x, y expected as str's"""
#    print '{0} * {1}'.format(X, Y)
    if len(X) < len(Y):
        temp = X
        X = Y
        Y = temp
    L, carry = [], 0
    for i, y in enumerate(reversed(Y)):
        R = [0 for j in range(i)]
        for j, x in enumerate(reversed(X)):
            temp = int(x) * int(y) + carry
            if temp > 9:
                carry = temp / 10
                temp = temp % 10
            else:
                carry = 0
            R.append(temp)
            if j == len(X) - 1 and carry:  # last one
                R.append(carry)
                carry = 0
        L.append(R)
        i += 1
    if len(L) == 1:
        if carry:
            R.append(carry)
        if reduce(lambda x, y: x + y, R) == 0:
            return '0'
        R = [str(r) for r in reversed(L[0])]
        return ''.join(R)
    def f(L):
        M = []
        for e in L:
            if e: M.append(e.pop(0))
        return M
    res, carry = [], 0
    while any(L):
        temp = sum(f(L)) + carry
        if temp > 9:
            carry = temp / 10
            res.append(temp % 10)
        else:
            carry = 0
            res.append(temp)
    if carry:
        res.append(carry)
    R = [str(r) for r in reversed(res)]
    return ''.join(R)


if __name__ == '__main__':
    N = 1000
    for i in range(N):
        for j in range(N):
            x = str(i * j)
            y = long_multiply(str(i), str(j))
            if x != y:
                print '{0} {1}: {2} {3}'.format(i, j, x, y)
#    L = ['2' for i in range(1000)]
#    M = [int(e) for e in reduce(long_multiply, L)]
#    print sum(M)
