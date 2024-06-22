class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        current_flip_state = 0

        for i in range(n):
            if (nums[i] == 0 and current_flip_state % 2 == 0) or (nums[i] == 1 and current_flip_state % 2 == 1):
                operations += 1
                current_flip_state += 1

        return operations
