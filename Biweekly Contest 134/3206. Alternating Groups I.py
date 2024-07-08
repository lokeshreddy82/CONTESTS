class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res=0
        n=len(colors)
        for i in range(len(colors)):
            if colors[i-1]==colors[(i+1)%n] and colors[i]!=colors[i-1]:
                res +=1
        return res
