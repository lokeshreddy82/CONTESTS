class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res=0
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                h=hours[i]+hours[j]
                if h%24==0:
                    res +=1
        return res
