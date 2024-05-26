class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        hashing={}
        countt=1
        for i in range(len(nums)):
            if nums[i]==x:
                hashing[countt]=i
                countt +=1
        res=[]
        for j in range(len(queries)):
            if hashing.get(queries[j],-1)!=-1:
                res.append(hashing[queries[j]])
            else:
                res.append(-1)
        return res
        