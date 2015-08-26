#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 024.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: lexicographic permutation

1. first permutate all the numbers or letters

2. order them by numerical or alphabetical


smart strategy:

http://www.cnblogs.com/xianglan/archive/2011/03/07/1976431.html

从1位到第N位之间的距离是N-1，通过发现序列之间变化数字能够产生多少变化

"""


import doctest
import operator
import itertools


def fac(n):
    '''
    >>> fac(4)
    24
    '''
    return reduce(operator.mul, [i for i in xrange(1, n+1)])


def get_the_permutation():
    '''
    >>> get_the_permutation()
    '2783915460'
    '''
    seq = range(10)
    N = 1000000 - 1
    factorial = [fac(i) for i in xrange(9, 0, -1)]
    steps = [0] * 9
    for i in xrange(9):
        steps[i] = N / factorial[i]
        N -= steps[i] * factorial[i]
    assert N == 0
    for i in xrange(9):
        seq[i], seq[i + steps[i]] = seq[i + steps[i]], seq[i]
        seq[(i+1):] = sorted(seq[(i+1):])
    return ''.join(map(str, seq))


def quick_sol():

    '''
    >>> quick_sol()
    '2783915460'
    '''
    N = 1000000
    # return ''.join(map(str, list(itertools.permutations(xrange(10)))[N-1]))
    permComb = itertools.permutations(xrange(10))
    while N:
        N -= 1
        res = permComb.next()
    return ''.join(map(str, res))

if __name__ == "__main__":
    doctest.testmod()
