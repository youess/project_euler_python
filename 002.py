#!/usr/bin/env python
# -*- coding: utf-8 -*-


import doctest


def fib_even_sum():
    """
    >>> fib_even_sum()
    4613732
    """
    a, b = 1, 2
    total = 2
    while 1:
        c = a + b
        if c > 4000000:
            break
        if not c & 1:
            total += c
        a = b
        b = c
    return total

if __name__ == "__main__":
    doctest.testmod()
    # fib_even_sum()
