#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 011.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: largest production in a grid
"""

import doctest
from operator import mul


def prod(l):
    return reduce(mul, l)


def get_grid_prod(array):

    m, n = len(array), len(array[0])
    total = 0

    for i in range(m):
        for j in range(n - 3):
            total = max(prod(array[i][j:(j + 3)]), total)

    for i in range(n):
        for j in range(m - 3):
            total = max(prod([array[j][i], array[j + 1][i],
                              array[j + 2][i], array[j + 3][i]
                              ]), total)

    for i in range(m - 3):
        for j in range(n - 3):
            diag_prod = max(prod([array[i][j], array[i + 1][j + 1],
                                  array[i + 2][j + 2], array[i + 3][j + 3]
                                  ]),
                            prod([array[i][j + 3], array[i + 1][j + 2],
                                  array[i + 2][j + 1], array[i + 3][j]])
                            )
            total = max(diag_prod, total)
    return total

if __name__ == "__main__":
    a = open("./grid_numbers_011.txt").read()
    a = [i.split() for i in a.split('\n')[:-1]]
    a = [map(int, i) for i in a]
    print get_grid_prod(a)           # 70600674
    doctest.testmod()
