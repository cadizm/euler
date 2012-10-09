#!/usr/bin/env python

#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#

# TODO: I'm really ugly, please fix me
def long_multiply(X, Y):
    """Long multiplication of x and y
    One of x or y must be of str length <= 2
    Result returned as str. Params x, y expected as str's"""
    if len(X) < len(Y):
        temp = X
        X = Y
        Y = temp
    carry, L = 0, []
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
            R.append(str(carry))
        if reduce(lambda x, y: x + y, R) == 0:
            return '0'
        R = [str(r) for r in reversed(L[0])]
        return ''.join(R)
    # TODO: unpack L into more than 2 lists
    # in order to supprt operand lengths > 2
    M, N = L
    L, carry = [], 0
    while M and N:
        m, n = M.pop(0), N.pop(0)
        temp = m + n + carry
        if temp > 9:
            carry = temp / 10
            L.append(temp % 10)
        else:
            carry = 0
            L.append(temp)
    Z = M if M else N
    if Z:
        for i, z in enumerate(Z):
            Z[i] += carry
            if Z[i] > 9:
                carry = Z[i] / 10
                Z[i] = Z[i] % 10
            else:
                carry = 0
            L.append(Z[i])
        if carry:
            L.append(carry)
    elif carry:
        L.append(carry)
    R = [str(r) for r in reversed(L)]
    return ''.join(R)


if __name__ == '__main__':
#    N = 100
#    for i in range(N):
#        for j in range(N):
#            x = str(i * j)
#            y = long_multiply(str(i), str(j))
#            if x != y:
#                print '{0} {1}: {2} {3}'.format(i, j, x, y)
    L = ['2' for i in range(1000)]
    M = [int(e) for e in reduce(long_multiply, L)]
    print sum(M)
