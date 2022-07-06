#!/usr/bin/python3
from re import I


def uniq_add(my_list=[]):
    new = set(my_list)
    res = 0
    for i in new:
        res += i
    return res
