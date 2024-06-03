class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n=len(nums1)
        m=len(nums2)
        maxx=max(nums1)
        hashing={}
        res=0
        for i in nums1:
            hashing[i]=hashing.get(i,0)+1
        for i in range(len(nums2)):
            every=nums2[i]*k
            j=2
            val=every
            if val==1:
                res +=n
                continue
            while val<=maxx:
                if hashing.get(val,0)!=0:
                    res +=hashing[val]
                val=every*j
                j +=1
        return res
