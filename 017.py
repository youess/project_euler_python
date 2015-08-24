#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 017.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: count number of english word length from 1 to 1000

http://blog.sina.com.cn/s/blog_ac9fdc0b0101lchv.html

"""

import doctest


_special_bits = {

    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

_special_teen = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

_special_ty = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}


def transNumUnder100(num):
    '''
    >>> transNumUnder100(99)
    'ninetynine'
    >>> transNumUnder100(12)
    'twelve'
    >>> transNumUnder100(1)
    'one'
    '''
    assert num > 0 and num < 100
    try:
        num_str = _special_teen[num]
    except KeyError:
        if num < 100 and num > 0:
            bit = num % 10
            ten = num / 10
            if ten and bit:
                num_str = _special_ty[ten] + '' + _special_bits[bit]
            elif ten == 0:
                num_str = _special_bits[bit]
            else:
                num_str = _special_ty[ten]
    return num_str


def transNumUnder1000(num):
    '''
    >>> transNumUnder1000(221)
    'twohundredandtwentyone'
    '''
    assert num > 0 and num <= 1000
    if num == 1000:
        num_str = 'onethousand'
    elif num < 100:
        num_str = transNumUnder100(num)
    else:
        ten = num % 100
        hundred = num / 100
        num_str = _special_bits[hundred] + 'hundredand' + transNumUnder100(ten) \
            if ten else _special_bits[hundred] + 'hundred'
    return num_str


def get_letters_sum(N):
    '''
    >>> get_letters_sum(1000)
    21124
    '''
    letter_sum = 0
    for i in xrange(1, N + 1):
        letter_sum += len(transNumUnder1000(i))
    return letter_sum


if __name__ == "__main__":
    doctest.testmod()
