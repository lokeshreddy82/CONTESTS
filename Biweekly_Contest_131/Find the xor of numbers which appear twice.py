from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        res=0
        hashing=Counter(nums)
        print(hashing)
        for i in range(len(nums)):
            if hashing.get(nums[i],0)==2:
                hashing[nums[i]]=hashing.get(nums[i])-1
                res^=nums[i]
        return res