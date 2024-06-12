class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()  
        ans = {0}  
        for r in rewardValues:
            new_rewards = set()
            for x in ans:
                if r > x:
                    new_rewards.add(x + r)
            ans.update(new_rewards)
        
        return max(ans)
class Solution:
    def maxTotalReward(self, nums: List[int]) -> int:
	nums=list(set(nums))
	nums.sort()
	@cache
	def dfs(i,curr):
	    if i>=len(nums):
		return curr
	    nottake=dfs(i+1,curr)
	    if nums[i]>curr:
		take=dfs(i+1,nums[i]+curr)
	    else:
		take=0
	    maxi=max(take,nottake)
	    return maxi
	return dfs(0,0)

