#!/usr/bin/env python


import os
import re


if __name__ == '__main__':
    problems = os.listdir(os.path.join('euler', 'problems'))
    problems = filter(lambda x: re.match(r'^p\d+\.py$', x), problems)
    problems = [p.rstrip('.py') for p in problems]

    module = getattr(__import__('euler'), 'problems')
    for p in problems:
        print '{0}:'.format(p),
        getattr(module, p).run()
