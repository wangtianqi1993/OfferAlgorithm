# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

def max_diff(numbers):
    if numbers is None or len(numbers)<2:
        return
    min  = numbers[0]
    max_diff = numbers[1] - min
    for i in range(2, len(numbers)):
        if numbers[i-1]<min:
            min = numbers[i-1]
        current_dif = numbers[i]-min
        if max_diff < current_dif:
            max_diff = current_dif
    print max_diff

def qsort(data):
    if data == []:
        return []
    else:
        pivot = data[0]
        litter = qsort([x for x in data[1:] if x<pivot])
        greater = qsort([x for x in data[1:] if x>=pivot])
        return litter+[pivot]+greater
seq = [5,6,78,9,0,-1,2,3,-56,13]
print qsort(seq)



