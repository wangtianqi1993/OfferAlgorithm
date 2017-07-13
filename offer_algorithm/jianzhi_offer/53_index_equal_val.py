# !/usr/bin/evn python
# -*-coding: utf-8 -*-
__author__ = 'wtq'

def get_index_equal_val(data):
    if data is None or len(data) == 0:
        return
    left = 0
    right = len(data)-1
    while left <= right:
        mid = (left+right)>>1
        if data[mid] == mid:
            return mid
        elif data[mid] < mid:
            left = mid+1
        else:
            right = mid-1
    return -1

data = [4,1,56]
print get_index_equal_val(data)
