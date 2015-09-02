#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 031.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: coin combination

mt => 1, 2, 5, 10, 20, 50, 100, 200

use dynamic programming

eg, 250
250 - mt 种
(250 - mt) - mt 种
....
一直可以递归下去

"""


import doctest


def coin_comb(mType, mMount):
    '''
    >>> coin_comb([1, 2, 5, 10, 20, 50, 100, 200], 200)
    73682
    '''
    mType.sort()
    mType_len = len(mType)
    comb = [0] * (mMount + 1)
    comb[0] = 1

    for index in xrange(mType_len):
        for m in xrange(mType[index], mMount + 1):
            comb[m] += comb[m - mType[index]]
    return comb[mMount]


if __name__ == "__main__":
    doctest.testmod()
