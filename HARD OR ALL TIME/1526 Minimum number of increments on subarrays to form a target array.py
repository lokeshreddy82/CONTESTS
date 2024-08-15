from itertools import pairwise
class Solution:
    def minNumberOperations(self, target: list[int], ans = 0) -> int:
        for prev, curr in pairwise(target):
            ans+= max(curr - prev, 0)
        return ans + target[0]  