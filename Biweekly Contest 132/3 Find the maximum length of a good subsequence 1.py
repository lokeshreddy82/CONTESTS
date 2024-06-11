class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)

        @cache
        def helper(k, i):
            if i >=n or k <0:
                return 0
            mx = 0
            for j in range(i+1, n):
                if nums[j] == nums[i]:
                    mx = max(mx, helper(k, j))
                else:
                    mx = max(mx, helper(k-1, j))
            return 1 + mx

        for i in range(n):
            ans = max(ans, helper(k, i))
        return ans
