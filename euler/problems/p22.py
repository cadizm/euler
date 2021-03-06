#!/usr/bin/env python

#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
# obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?
#
#
# TODO: use an external sort to handle very large files
#   (http://en.wikipedia.org/wiki/External_sorting)
#


from euler.misc import name_score

import string
import os


def run():
    data_dir = '{0}/../data'.format(os.path.dirname(__file__))
    names = []
    for line in open(os.path.join(data_dir, 'names.txt'), 'r'):
        names.extend([name.lower().strip('"') for name in line.split(',')])
    print name_score(names)
