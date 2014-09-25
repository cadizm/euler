#!/usr/bin/env python


import string


ONE_THRU_NINE = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

TEN_THRU_NINETEEN = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]

TWENTY_THRU_NINETY_BASE = [
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]

HUNDRED_BASE = [
    'hundred',
]

THOUSAND_BASE = [
    'thousand',
]


def letter_counts():
    S = 0
    # 1-9
    for a in ONE_THRU_NINE:
        S += len(a)
    # 10-19
    for a in TEN_THRU_NINETEEN:
        S += len(a)
    # 20-99
    for a in TWENTY_THRU_NINETY_BASE:
        S += len(a)
        for b in ONE_THRU_NINE:
            S += len(a + b)
    # 100-999
    for a in ONE_THRU_NINE:
        for b in HUNDRED_BASE:
            S += len(a + b)
            for c in ONE_THRU_NINE:
                S += len(a + b + 'and' + c)
            for c in TEN_THRU_NINETEEN:
                S += len(a + b + 'and' + c)
            for c in TWENTY_THRU_NINETY_BASE:
                S += len(a + b + 'and' + c)
                for d in ONE_THRU_NINE:
                    S += len(a + b + 'and' + c + d)
    # 1000
    S += len(ONE_THRU_NINE[0] + THOUSAND_BASE[0])
    return S


def name_score(names):
    value = {}
    for i, v in enumerate(string.lowercase, start=1):
        value[v] = i
    def score(index, name):
        return sum([value[letter] for letter in name]) * index
    S = 0
    for i, v in enumerate(sorted(names), start=1):
        S += score(i, v)
    return S


def diagonal_sum(N):
    """Sum of diagonals in an NxN grid
    """
    upper_right, lower_right, sum_diag = 1, 1, -3
    i, n_by_n = 0, 1
    while True:
        lower_right = upper_right + (2 * i)
        upper_right = upper_right + (8 * i)
        sum_diag += 2 * (upper_right + lower_right)
        if n_by_n >= N:
            break
        else:
            i, n_by_n = i + 1, n_by_n + 2
    return n_by_n, sum_diag
