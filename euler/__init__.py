
__all__ = [
    'graph',
    'grid',
    'math',
    'memoize',
    'misc',
    'problems',
    'test',
    'triangle',
    'util',
]

[__import__('euler.{0}'.format(m)) for m in __all__]
