# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'


def get_max_unrepeat(str):
    if str is None:
        return str
    max_len = 0
    index = 0
    for i in range(len(str)):
        str_map = {}
        for j in range(i, len(str)):
            if str[j] not in str_map:
                str_map[str[j]] = 1
            else:
                break
        if max_len < j-i:
            max_len = j-i
            index = i

    print index, max_len
    print str[index:index+max_len]

s = 'abcdefasd'
get_max_unrepeat(s)
a = ['1','2','3']
print "_".join(a)
