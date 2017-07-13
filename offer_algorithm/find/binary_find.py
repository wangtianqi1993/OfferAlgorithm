# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

def binary_find(data, obj):
    start = 0
    end = len(data)
    while start <= end:
        mid = (start+end)>>2
        if data[mid] == obj:
            print mid
            return
        elif data[mid]>obj:
            end = mid-1
        else:
            start = mid+1


def lower_bound_find(data, obj):
    """
    data中有重复的数据，找到值为obj的下标的最小值，找到的是大于等于obj的第一个数的下标
    :param data:
    :param obj:
    :return:
    """
    start = 0
    end = len(data)
    while end>0:
        half = end>>1
        mid = start + half
        if data[mid]<obj:
            start = mid+1
            end = end-half-1
        else:
            end = half
    print start

data = [1,2,7,8,10]
lower_bound_find(data, 9)
