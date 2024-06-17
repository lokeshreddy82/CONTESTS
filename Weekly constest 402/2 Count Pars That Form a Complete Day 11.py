class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res=0
        from collections import defaultdict
        remainder_count=defaultdict(int)
        count_pairs = 0
    
        for hour in hours:
            rem = hour % 24
            comp = (24 - rem) % 24

            if comp in remainder_count:
                count_pairs += remainder_count[comp]

            remainder_count[rem] += 1

        return count_pairs
