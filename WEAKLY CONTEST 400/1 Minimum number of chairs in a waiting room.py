class Solution:
    def minimumChairs(self, s: str) -> int:
        res=0
        chairs=0
        empty=0
        for i in s:
            if i=="E":
                chairs +=1
            else:
                if chairs:
                    chairs -=1
            res=max(res,chairs)
        res=max(res,chairs)
        return res
s=Solution()
print(s.minimumChairs("ELEELEELLL"))