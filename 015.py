#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 015.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: the number of path in a grid
有三种解法，一种是递归，起点到(m, n)的路径 = 起点到(m-1, n) + 起点到(m, n-1)
第二种是迭代，解决上一步骤需要用的额外空间，本质都是属于动态规划
第三种是组合方式，向右和向下走的步骤总共是m + n次，向右走m次，
所以总共等于C^(m)_(m + n)
"""

import doctest
import numpy as np


# cache recursion
def solution1():
    '''
    >>> int(solution1())
    137846528820
    '''
    m, n = 20, 20
    cache = np.zeros((m + 1, n + 1))
    cache[0] = 1
    cache = cache.T
    cache[0] = 1
    cache = cache.T

    def routes(r, c):
        if r == 0 or c == 0:
            return 1
        if cache[r][c]:
            return cache[r][c]
        cache[r][c] = routes(r-1, c) + routes(r, c-1)
        return cache[r][c]
    routes(m, n)
    return cache[m][n]


# iteration, dynamic programming
def solution2():
    '''
    >>> int(solution2())
    137846528820
    '''
    m, n = 20, 20
    cache = np.zeros((m + 1, n + 1))
    cache[0] = 1
    cache = cache.T
    cache[0] = 1
    cache = cache.T

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]

    return cache[m][n]


# combination solution
def solution3():
    '''
    >>> solution3()
    137846528820
    '''
    from scipy.misc import comb
    print comb(40, 20, exact=True)


if __name__ == "__main__":
    doctest.testmod()
