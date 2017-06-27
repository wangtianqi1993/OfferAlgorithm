# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'


def count_sort(data):
    """
    非比较排序时间复杂度为O(n)
    :param data:
    :return:
    """
    min_data = min(data)
    max_data = max(data)
    len_data = max_data - min_data + 1
    store = [0]*len_data
    for i in data:
        store[i-min_data] += 1

    for index in range(len(store)):
        while store[index]:
            print index + min_data
            store[index] -= 1

test = [6, 2, 1, 3, 5, 6, 5, 4]
count_sort(test)
