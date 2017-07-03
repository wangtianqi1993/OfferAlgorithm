def isNumeric(s):
    # write code here
    if s is None:
        return False
    if len(s) == 0:
        return False
    if s[-1] == 'e' or s[-1] == 'E':
        return False

    point_count = 0
    e_count = 0
    for index in range(len(s)):
        if index == 0:
            if s[index] == "+" or s[index] == "-":
                continue
        else:
            if (s[index] == "+" or s[index] == "-") and (s[index-1]=="e" or s[index-1]=="E"):
                continue
            if s[index] == '.' and index < len(s)-1:
                point_count += 1
                continue
            if point_count > 1:
                return False

            if (s[index] == "e" or s[index] == "E") and index < len(s)-1:
                e_count += 1
                continue
            if e_count > 1:
                return False

            if s[index] > '9' or s[index] < '0':
                return False
    return True


def test(a):
    a.add(2)


def permutation(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in permutation(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = map(self.convert, timePoints)
        minutes.sort()
        print minutes
        for x, y in zip(minutes, minutes[1:] + minutes[:1]):
            print y, x, (y-x)%(24*60)
        return min((y-x) % (24*60) for x, y in zip(minutes, minutes[1:] + minutes[:1]))

    def convert(self, times):
        return int(times[:2])*60 + int(times[3:])


def subseq(w1, w2):
    i = 0
    for c in w2:
        if i < len(w1) and w1[i] == c:
            i+=1
    return i == len(w1)


def subseq1(w1, w2):
    if w1 in w2:
        return True
    else:
        return False


def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vio = ['a','e','i','o','u','A','E','I','O','U']

    start = 0
    end = len(s)-1
    s = list(s)
    while start <= end:
        print s[start]
        print start, end

        if s[start] in vio and s[end] in vio:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        if start > end:
            break
        if s[start] not in vio:
            start += 1
        if s[end] not in vio:
            end -= 1
    return "".join(s)

from itertools import combinations


class Solution(object):
    def __init__(self):
        self.count = 0

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
             return 0
        if s == t:
            return 1
        for item in combinations(range(len(s)), len(t)):
            temp = [s[i] for i in item]
            print temp
            if "".join(temp) == t:
                self.count += 1
        return self.count


def test_ss():
    s1 = int(raw_input())
    s2 = int(raw_input())
    if s1>s2:
        print "GREATER"
    elif s1 == s2:
        print "EQUAL"
    else:
        print "LESS"


def check_ip(s):
    if s is None or len(s) < 4 or len(s) > 12:
        return []
    result = []
    weights = []
    s = list(s)
    len_s = len(s)

    for i in range(1, 4):
        for j in range(1, 4):
            for m in range(1, 4):
                for n in range(1, 4):
                    if i + j + m + n == len_s:
                        weights.append([i,j,m,n])
    for i in weights:
        if 0<=change(s[0:i[0]])<=255 and 0<=change(s[i[0]:i[0]+i[1]])<=255 and 0<=change(s[i[0]+i[1]:i[0]+i[1]+i[2]])<=255 and 0<=change(s[i[0]+i[1]+i[2]:i[0]+i[1]+i[2]+i[3]])<=255:
            temp_ip = "".join(s[0:i[0]]) + "." + "".join(s[i[0]:i[0]+i[1]]) + "." + "".join(s[i[0]+i[1]:i[0]+i[1]+i[2]]) + "." + "".join(s[i[0]+i[1]+i[2]:i[0]+i[1]+i[2]+i[3]])
            result.append(temp_ip)
    return result


def change(s):
    return int("".join(s))

class Solution(object):
    def pailromPairs(self, words):
        wmap = {y:x for x, y in enumerate(words)}
        def isdrom(word):
            size = len(word)
            for x in range(size/2):
                if word[x] != word[size-x-1]:
                    return False
            return True

        ans = set()
        for idx, word in enumerate(words):

            if "" in wmap and word != "" and isdrom(word):
                bidx = wmap[""]
                ans.add((bidx, idx))
                ans.add((idx, bidx))
            rword = word[::-1]

            if rword in wmap:
                ridx = wmap[rword]
                if idx != ridx:
                    ans.add((idx, ridx))
                    ans.add((ridx, idx))

            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                rleft, rright = left[::-1], right[::-1]
                if isdrom(left) and rright in wmap:
                    ans.add((wmap[rright], idx))
                if isdrom(right) and rleft in wmap:
                    ans.add((idx, wmap[left]))
        return list(ans)

def getSize(h):
    c =0
    while h:
        c += 1
        h = h.next
    return c


def calculate_augly(s_in):

    if s_in is None:
        return 0
    s = [i for i in s_in]

    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 0
    for i in range(1, len(s)):
        if s[i] == "?":
            if s[i-1] == "A":
                s[i] = "B"
            if s[i-1] == "B":
                s[i] = 'A'
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    return count

num = "A?AAAA"
print calculate_augly(num)
s = 'szdsd'
S = s.upper()
print S

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    start = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[start] = nums[i]
            start += 1
    print nums
