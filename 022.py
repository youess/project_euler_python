#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 022.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: names score,

first sum the alphabetical order and multiple its index in the file list
"""


import doctest


def letter2int(letter):
    '''make the letter be lower case'''
    return ord(letter.lower()) - 96


def sumWord(word):
    '''
    >>> sumWord('COLIN')
    53
    '''
    return sum([letter2int(i) for i in word])


def cal_name_score(l):
    '''
    >>> cal_name_score(names)
    871198282
    '''
    return sum([(i + 1) * sumWord(j) for i, j in enumerate(l)])


if __name__ == "__main__":
    with open('./p022_names.txt') as f:
        names = f.read()

    names = map(lambda x: x.strip('"'), names.split(","))
    names.sort()
    # print names.index('COLIN')
    doctest.testmod()
