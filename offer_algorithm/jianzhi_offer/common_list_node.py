# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return

        other2 = pHead2
        other1 = pHead1
        length1 = self.getListLength(other1)
        length2 = self.getListLength(other2)

        if length1 > length2:
            for i in range(abs(length1 - length2)):
                pHead1 = pHead1.next
        else:
            for i in range(abs(length1 - length2)):
                pHead2 = pHead2.next

        while pHead1 and pHead2 and pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        print pHead1

    def getListLength(self, p1):
        length = 0
        while p1:
            length += 1
            p1 = p1.next
        return length

if __name__ == "__main__":
    l1 = ListNode(0)
    l2 = ListNode(1)
    temp1 = l1
    temp2 = l2

    for i in range(5):
        temp = ListNode(i)
        temp1.next = temp
        temp1 = temp
    for i in range(4):
        temp = ListNode(i)
        temp1.next = temp
        temp1 = temp
    s = Solution()
    s.FindFirstCommonNode(l1, l2)
