#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 10 Warmup Task 7"""


DATA = {
    2: 13,
    11: 24,
    5: 7,
    10: 23,
    8: 29,
    7: 30,
    4: 3,
    6: 25,
    12: 31,
    1: 27
}


def iter_dict_funky_sum(mydict):
    """Loops dictionary extracting keys and values and summing together.

    Args:
       mydict(dict): A dictionary with an int for both key and value.

    Returns:
        int: Sums all values in dictionary minus key

    Examples:

    >>> iter_dict_funky_sum(DATA)
    146
    """
    total = 0
    for key, value in mydict.iteritems():
        total += value-key
    return total
