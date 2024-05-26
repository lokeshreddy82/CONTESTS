class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        res=[]
        hashing={}
        colors={}
        for val,col in queries:
            if hashing.get(val,-1)!=-1:
                colors[hashing.get(val)]=colors.get(hashing.get(val))-1
                if colors[hashing.get(val)]==0:
                    del colors[hashing.get(val)]
            hashing[val]=col
            colors[col]=colors.get(col,0)+1
            res.append(min(len(hashing),len(colors)))
        return res
s=Solution()
print(s.queryResults(4, [[1,4],[2,5],[1,3],[3,4]]))