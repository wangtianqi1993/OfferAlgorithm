__author__ = 'wtq'


def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))


def strictly_decreasing(L):
    return all(x>y for x, y in zip(L, L[1:]))

n = int(raw_input())
data = map(int, raw_input().split())
if n == 0:
    print 0
else:
    count = 1
    sign = 0
    for i in range(1, n):
    	if data[i] < data[i-1]:
            if sign == 0:
                sign = -1
            if sign == 1:
                sign = 0
                count += 1
        elif data[i] > data[i-1]:
            if sign ==0:
                sign = 1
            if sign == -1:
                sign = 0
                count += 1
        print data[i], count, sign

    print count
