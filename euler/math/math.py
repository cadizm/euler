#!/usr/bin/env python


from .primes import is_prime
from .primes import eratosthenes
from euler.memoize import memoize


def is_repeating_decimal(numerator, denominator):
    """
    """
    pass
    #repeating_decimals = [i for i in range(2, 1000) if
    #        filter(lambda x: x not in [2, 5], prime_factors(i))]
    #print repeating_decimals


def long_multiplication(X, Y):
    """
    Long multiplication of X and Y
    Result returned as str. Params x, y expected as str's
    """
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



def long_division(numerator, denominator):
    """Compute n divided by d using long division
    """

    # TODO:
    #   - handle cases where numerator > denominator
    #   - put numerator / denominator in lowest terms

    res, initial_remainder, remainders = '', 0, []
    remainder = numerator
    cycle, repeating = None, None

    while remainder:
        while remainder < denominator:
            remainder *= 10
            if remainder < denominator:
                res += '0'
        if not initial_remainder:
            initial_remainder = remainder
        elif remainder == initial_remainder: # we found a cycle
            cycle = res
            remainder = 0
            break

        digit = remainder / denominator
        res += str(digit)
        remainder -= denominator * digit

        if remainder == repeating:  # we found a repeating decimal
            cycle = str(digit)
            remainder = 0
        else:
            repeating = remainder
        if remainder in remainders: # we found a cyclde
            cycle = res
            remainder = 0
            break
        else:
            remainders.append(remainder)

    res = '.{0}'.format(res)
    if cycle:
        res = res.replace(cycle, '({0})'.format(cycle))
    return res


def factorize(n, P=eratosthenes(1000)):
    """Integer factorization of n using list of primes P
    Return list of tuples of prime factors. e.g.:
    [(2, 3), (3, 2)] = 2^3 * 3^2 = 72
    """
    F, N = [], n
    for p in P:
        e = 0
        while n % p == 0:
            e += 1
            n /= p
        if e:
            F.append((p, e))
    return F


def ndivisors(n, P=eratosthenes(1000)):
    """Compute number of divisors
    http://primes.utm.edu/glossary/xpage/tau.html
    """
    if n < 0:
        return 0
    elif n == 1:
        return 1
    elif n in P:
        return 2
    F = factorize(n, P)
    E = [e + 1 for p, e in F]
    return reduce(lambda x, y: x * y, E)


def collatz(n, d={}):
    """http://en.wikipedia.org/wiki/Collatz_conjecture
    Implementation note: memoize results into dict d
    """
    if n in d:
        return d[n]
    N, i = n, 0
    while N > 1:
        if N in d:
            d[n] = d[N] + i
            return d[n]
        i += 1
        if N % 2 == 0:
            N /= 2
        else:
            N = 3 * N + 1
    d[n] = i + 1
    return i + 1


def iterative_factorial(n):
    if n < 0:
        return None
    if n in [0, 1]:
        return 1
    for i in range(1, n):
        n *= i
    return n


@memoize
def recursive_factorial(n):
    if n < 0:
        return None
    if n in [0, 1]:
        return 1
    return n * recursive_factorial(n - 1)


def sum_factorial_digits(N):
    return sum([recursive_factorial(i) for i in digits(N)])


def central_binomial_coefficient(n):
    return iterative_factorial(2 * n) / (iterative_factorial(n))**2


@memoize
def proper_divisors(N):
    L = []
    for i in range(1, (N / 2) + 1):
        if N % i == 0:
            L.append(i)
    return L


def abundant_sum(limit=28123):
    perfect, deficient, abundant = ([], [], [])
    for i in range(limit):
        n = sum(proper_divisors(i))
        if n < i:
            L = deficient
        elif n > i:
            L = abundant
        else:
            L = perfect
        L.append(i)
    two_abundant = {}
    for a in abundant:
        for b in abundant:
            two_abundant[a + b] = 1
    N = 0
    for i in range(limit):
        if i not in two_abundant:
            N += i
    return N


def digits(N):
    n = N
    res = []
    while n > 0:
        d = n % 10
        res.insert(0, d)
        n = n / 10
    return res


def ndigits(N):
    n, i = N, 0
    while n > 0:
        n, i = n / 10, i + 1
    return i


def ndigits_list(N):
    """Return number of digits in N plus the digits themselves
    """
    n, i, L = N, 1, []
    while n >= 10:
        L.append(n % 10)
        n /= 10
        i += 1
    return i, [n] + L


def quadratic(n, a, b):
    return (n * n) + (a * n) + b


def quadratic_range(N, A, B):
    coeff_a, coeff_b, nprimes = None, None, 0
    for a in range(-A, A):
        for b in range(-B, B):
            for n in range(N):
                q = quadratic(n, a, b)
                if not is_prime(q):
                    break
                elif n > nprimes:
                    coeff_a, coeff_b, nprimes = a, b, n + 1
    return coeff_a, coeff_b, nprimes


def distinct_powers(lower, upper):
    M, N = lower, upper
    d = {}
    for i in range(M, N):
        prev, cur = i, None
        for j in range(M, N):
            if i == M:
                cur = i**j
            else:
                cur = prev * i
                prev = cur
            d[cur] = 1
    return len(d.keys())


def narcissistic_upper(n):
    """Computer loose upper bound for n-digit narcissistic number
    """
    return (n + 1) * (9**n)


def is_narcissistic(N):
    n = N
    L = []
    while n > 0:
        d = n % 10
        n = n / 10
        L.append(d)
    p = len(L)
    return sum([e**p for e in L]) == N


def nth_power_digit_sum(n, N):
    """nth power sum of each digit in N
    """
    temp = N
    L = []
    while temp > 0:
        d = temp % 10
        temp = temp / 10
        L.append(d)
    return sum([e**n for e in L])


def champernowne_constant(expr):
    """http://en.wikipedia.org/wiki/Champernowne_constant
    """
    n, res = 0, 1
    for i in range(expr[-1] + 1):
        m, L = ndigits_list(i)
        M = range(n, n + len(L))
        for j, k in enumerate(M):
            if k in expr:
                res *= L[j]
        n += m
    return res


def gcd(a, b):
    """Euclid's algorithm
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    """Reduction by gcd
    """
    return (a * b) / gcd(a, b)


def smallest_multiple(lower, upper):
    n = 1
    for i in range(lower, upper):
        n = lcm(i, n)
    return n


def square_sum(n):
    """Return sum of the first n numbers, squared
    """
    return ((n * (n + 1)) / 2)**2


def square_pyramid(n):
    """
    Return nth square pyramid number

    This is equivalent to the sum of first n square numbers
    """
    return (n * (n + 1) * ((2 * n) + 1)) / 6


def max_product_in_series(L, window_size=13):
    start = 0
    end = start + window_size
    W = [e for e in L[start:end]]
    max_prod = reduce(lambda x, y: x * y, W)
    prod = max_prod
    while True:
        if end == len(L):
            break
        h = W.pop(0)
        t = L[end]
        W.append(t)
        if 0 not in W and h:
            prod = prod / h * t
            if prod > max_prod:
                max_prod = prod
        else:
            prod = reduce(lambda x, y: x * y, W)
        end += 1
    return max_prod


def pythagorean_triplet(n):
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            c = 1000 - (a + b)
            if a**2 + b**2 == c**2:
                return a * b * c
