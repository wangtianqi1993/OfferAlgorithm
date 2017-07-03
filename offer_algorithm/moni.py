
def split_s(s1):
    s = [i for i in s1]
    len_s1 = len(s)
    if len_s1 <= 8:
        for i in range(8-len_s1):
            s.append("0")
        print "".join(s)
    else:
        times = len_s1/8
        j=0
        for i in range(times):
            tmp = s[j:j+8]
            print "".join(tmp)
            j+=8
        tmp = s[j:]
        if len(tmp)>0:
            for i in range(8-len(tmp)):
                tmp.append("0")

            print "".join(tmp)
        
s1 = raw_input()
s2 = raw_input()

split_s(s1)
split_s(s2)
