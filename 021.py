#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 021.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: amicable number

d(n) defined as the sum of its divisors(not include n itself),

if d(a) = b and d(b) = a, and a != b, then a, b called as
an amicable number pair

"""


import doctest


def divisor_sum(num):
    '''sum the proper divisor of the num (not include num)
    >>> divisor_sum(220)
    284
    '''
    assert num > 0
    total = 0
    for i in xrange(1, num):
        if num % i == 0:
            total += i
    return total


def amicable_num_sum(limit):
    '''
    >>> amicable_num_sum(10000)
    31626
    '''
    amicable_pair = []
    cache = []
    for a in range(2, limit):
        try:
            cache.index(a)
            continue
        except ValueError:
            b = divisor_sum(a)
            if a != b and a == divisor_sum(b):
                amicable_pair.append((a, b))
                cache.append(b)
    # print amicable_pair
    return sum([sum(i) for i in amicable_pair])


if __name__ == "__main__":
    doctest.testmod()
