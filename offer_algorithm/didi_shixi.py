# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

import sys


def maxEnvelopes(envelopes):
    # Write your code here
    c = [i for i in envelopes]
    print sorted(c, key = lambda x: (x[0], -x[1]))
    height = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
    dp, length = [0] * len(height), 0
    print "height", height
    import bisect
    for h in height:
        i = bisect.bisect_left(dp, h, 0, length)
        print 'i', i
        dp[i] = h
        if i == length:
            length += 1
    return length


def mySolution(data):
    count = 0
    data.sort(key= lambda x:x[0])
    item1 = data[0]
    sign = 0
    while item1 != data[-1]:
        for item in data:
            if item1[0] < item[0] and item1[1] < item[1]:
                count += 1
                item1 = item
                sign = 1
        if sign == 0:
            break
    if sign == 1:
        count += 1
    print count


if __name__ == "__main__":
    line = sys.stdin.readline()
    num = int(line.strip())
    data = []
    for i in range(num):
        temp = []
        line = sys.stdin.readline()
        line = line.split(" ")
        temp.append(int(line[0]))
        temp.append(int(line[1]))
        data.append(temp)
    print maxEnvelopes(data)
    #mySolution(data)
