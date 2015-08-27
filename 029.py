#!/usr/bin/env python
#-*- coding: utf8 -*-


'''
as python support big integer, so its simple to use brute-force

other options:

1. you can use log scale to calculate

2. http://www.mathblog.dk/project-euler-29-distinct-terms-sequence-ab/

'''


import doctest


def get_distinct_power_num(a, b):

    '''
    >>> get_distinct_power_num(5, 5)
    15
    >>> get_distinct_power_num(100, 100)
    9183
    '''
    s = set()
    for i in xrange(2, a+1):
        for j in xrange(2, b+1):
            s.add(i**j)
    return len(s)


def get_tuple(i, j):

    '''
    >>> get_tuple(8, 2)
    (2, 6)
    >>> get_tuple(49, 2)
    (7, 4)
    '''
    base = [2, 3, 5, 6, 7, 10]
    while base:
        b = base.pop()
        index = 0
        tmp = i
        while tmp / b:
            index += 1
            tmp /= b
        if b**index == i:
            j *= index
            i = b
            break
    return (i, j)


def get_distinct_power_num2(a, b):
    '''
    >>> get_distinct_power_num2(100, 100)
    9183
    '''
    s = set()
    for i in xrange(2, a+1):
        for j in xrange(2, b+1):
            s.add(get_tuple(i, j))
    return len(s)


if __name__ == "__main__":
    doctest.testmod()
