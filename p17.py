#!/usr/bin/env python

#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.
#

ONE_THRU_NINE = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine', ]

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
    'nineteen', ]

TWENTY_THRU_NINETY_BASE = [
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety', ]

HUNDRED_BASE = [
    'hundred', ]

THOUSAND_BASE = [
    'thousand', ]


if __name__ == '__main__':
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
    print S
