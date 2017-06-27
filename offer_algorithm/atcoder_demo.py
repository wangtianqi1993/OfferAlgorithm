# -*- coding: utf-8 -*-
__author__ = 'wtq'


def test():
    """
    input frame:
    5
    1 2 3 4 5
    :return:
    """
    n = int(raw_input())
    data = map(int, raw_input().split(" "))
    print n
    print data


def shortestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    def ispalin(s):
        for i in range(len(s)/2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

    if len(s) == 1 or s is None:
        return s

    for i in range(len(s)-2, 0, -1):
        print i
        if ispalin(s[:i+1]):
            print s[i+1:], s[:i+1]
            return s[i+1:][::-1] + s
    print "yse"
    return s[1:][::-1] + s


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if s is None:
        return False
    s = s.lower()
    s = [i for i in s if i.isdigit() or i.isalpha()]
    print s

    s = "".join(s)
    print s
    if s == s[::-1]:
        return True
    else:
        return False

tables, batch_num = map(int, raw_input().split(" "))
table_stores = map(int, raw_input().split(" "))
batch_store = []
for i in range(batch_num):
    temp = map(int, raw_input().split(" "))
    batch_store.append(temp)

table_stores.sort()
batch_store.sort(key=lambda x:x[1], reverse=True)
max_value = 0

for item in batch_store:
    sign = 0
    for index in range(len(table_stores)):
        if table_stores[index] >= item[0]:
            max_value += item[1]
            sign = 1
            break
    if sign == 1:
        table_stores.pop(index)
print max_value

