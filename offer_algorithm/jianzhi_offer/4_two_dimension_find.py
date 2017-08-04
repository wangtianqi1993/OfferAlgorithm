# !/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'wtq'


def matrix_search(matrix, obj):
    if matrix is None:
        return False

    col = len(matrix[0])-1
    row = 0
    while row<len(matrix) and col>=0:
        if matrix[row][col] == obj:
            return True
        elif matrix[row][col]>obj:
            col = col-1
        else:
            row = row+1
    return False

data = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print matrix_search(data, 6)
d = [1,2,2,1]
a = [i for i in d]
d.reverse()
if a == d:
    print 1

n = int(raw_input())
data = map(int, raw_input().split(" "))
def huiwen_times(data, start, end):
    times = 0
    left = data[start]
    right = data[end]
    while start < end:
        if left == right:
            start += 1
            end -= 1
            left = data[start]
            right = data[end]

	elif left < right:
            start += 1
            left += data[start]
            times += 1
            continue

        elif left > right:
            end -= 1
            right += data[end]
            times += 1
            continue

    print times

huiwen_times(data, 0, len(data)-1)
