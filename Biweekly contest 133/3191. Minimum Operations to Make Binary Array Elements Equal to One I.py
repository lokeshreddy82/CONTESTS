class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0

        for i in range(n - 2):
            if nums[i] == 0:
                # Flip the current element and the next two elements
                for j in range(3):
                    nums[i + j] = 1 - nums[i + j]
                operations += 1

        # Check if there are any 0s left in the last two elements
        if nums[-1] == 0 or nums[-2] == 0:
            return -1

        return operations
