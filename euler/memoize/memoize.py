#!/usr/bin/env python


from exceptions import KeyError


class memoize(object):
    """Memoization decorator (@memoize).
    """
    def __init__(self, func):
        self.func = func
        self.memo = dict()

    def __call__(self, *args):
        try:
            return self.memo[args]
        except KeyError:
            self.memo[args] = self.func(*args)
            return self.memo[args]
