class Solution:
    def maximumPoints(self, enemyEnergies: List[int], curr: int) -> int:
        res=0
        queue=sorted(enemyEnergies)
        while queue:
            if res and curr<queue[0]:
                curr +=queue.pop()
            elif curr>=queue[0]:
                res +=curr//queue[0]
                curr=curr%queue[0]
            else:
                break
        return res
