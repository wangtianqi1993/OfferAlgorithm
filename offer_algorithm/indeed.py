# -*-coding:utf-8 -*-
__author__ = 'wtq'

import itertools

def indeed_2():
    n, k, m = map(int, raw_input().split())
    relus = []
    result = []

    for i in range(m):
        temp = map(int, raw_input().split())
        relus.append(temp)

    indexs = itertools.permutations(range(m))
    for item in indexs:
        med1 = set()
        med2 = set()
        m1_sum = 0
        m2_sum = 0

        for i in item:
            sub = relus[i]
            if len(med1) < k:
                if sub[0] not in med2 and sub[1] not in med2 and sub[0] not in med1 and sub[1] not in med1:
                    med1.add(sub[0])
                    med1.add(sub[1])
                    m1_sum += sub[2]

            if len(med2) < k:
                if sub[0] not in med1 and sub[1] not in med1 and sub[0] not in med2 and sub[1] not in med2:
                    med2.add(sub[0])
                    med2.add(sub[1])
                    m2_sum += sub[2]

        result.append(m1_sum+m2_sum)
    print max(result)


def getValue(W, V, MAX, i):
    global count
    count = count + 1
    print count
    if i>1:
        notV, notW = getValue(W, V, MAX, i-1)
        if W[i-1] > MAX:
            return notV, notW
        else:
            changeV, changeW = getValue(W, V, MAX-W[i-1], i-1)
            if changeV + V[i-1] > notV:
                return changeV + V[i-1], changeW
            else:
                return notV, notW

    else:
        if (W[0]>MAX):
            return 0, MAX
        else:
            return V[0],MAX-W[0]


def goodIdea():
    V = [10, 40, 30, 50]
    W = [5, 4, 6, 3]
    MAX = 10
    print getValue(W, V, MAX, 4)

count = 0
goodIdea()
a = "esfdsfDDFF"
b = a.upper()
print b


l=[]
def All(str1):
    for i in str1:
        tmp=str1.replace(i,'')
        l.append(i)
        if len(tmp)>1:
            All(tmp)
            del l[-1]
        else:
            print ''.join(l)+tmp
            del l[-1]
All("ABC")

