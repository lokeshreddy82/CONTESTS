class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        a = Counter(power)
        power = sorted(list(set(power)))
        @cache
        def solve(curr):
            if curr>=len(power):
                return 0
            return max(power[curr]*a[power[curr]]+solve(bisect.bisect_right(power,power[curr]+2)),solve(curr+1))
        return solve(0)
        
