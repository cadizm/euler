#!/usr/bin/env python

#
# Each new term in the Fibonacci sequence is generated by adding the previous 
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms.
#

if __name__ == '__main__':
    N = [1, 2]
    while True:
        if N[-1] + N[-2] > 4000000:
            break
        N.append(N[-1] + N[-2])
    print sum([n for n in N if n % 2 == 0])
