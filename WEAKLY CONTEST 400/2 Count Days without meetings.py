class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res=0
        meetings.sort()
        prev=0
        print(meetings)
        for i in meetings:
            u=i[0]
            v=i[1]
            if  prev+1<u:
                res +=u-(prev+1)
            prev=max(prev,v)
        if prev<days:
            res +=days-prev
        return res