# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'


def getNext(pattern):
    j = 0
    next = []
    plen = len(pattern)
    next.append(0)
    for i in range(1, plen):
        while ((j > 0) and (pattern[i] != pattern[j])):
            j = next[j-1]
        if (pattern[i] == pattern[j]):
            j = j + 1
        next.append(j)
    print next
    return next

s = "aacecaaa"
new_s = s + "#" + s[::-1]
getNext(new_s)


def kmp_search(text, pattern):
    j = 0
    plen = len(pattern)
    tlen = len(text)
    next = getNext(pattern)
    for i in range(0, tlen):
        while j > 0 and text[i] != pattern[j]:
            j = next[j-1]

        if text[i] == pattern[j]:
            j = j + 1

        if j == plen:
            return True
    return False


def shortestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    A = s + "*" + s[::-1]
    print "A", A
    count = [0]
    for i in range(1, len(A)):
        index = count[i-1]
        while (index > 0 and A[index] != A[i]):
            index = count[index-1]
        count.append(index+(1 if A[index] == A[i] else 0))
    print 'count', count
    return s[count[-1]:][::-1]+s

getNext("babsf")
shortestPalindrome("bacsf")

print kmp_search("aaaaaaaabadfsds", "aaa")

import numpy as np
np.dot()
