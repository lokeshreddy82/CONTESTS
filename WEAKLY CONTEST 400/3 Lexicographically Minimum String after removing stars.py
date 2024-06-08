import sortedcontainers as n
from collections import defaultdict
class Solution:
    def clearStars(self, s:str)->str:
        res=""
        hashing=defaultdict(list)
        queue=[0]*26
        priority=n.SortedList()
        k=list(s)
        for i in range(len(s)):
            if s[i]=="*":
                c=priority.pop(0)
                ind=hashing[c].pop()
                k[ind]=""
                k[i]=""
            else:
                c=ord(s[i])
                hashing[c].append(i)
                priority.add(c)
                k[i]=s[i]
        return "".join(k)

