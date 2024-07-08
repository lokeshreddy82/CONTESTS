class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = 0
        arr = []
        n = len(colors)
        for i in range(1, k):
            if colors[i] == colors[i - 1]:
                arr.append(i - 1)
        
        if not arr:
            res += 1
        r=k
        for l in range(1,n):
            while colors[r%n]==colors[(r-1)%n]:
                arr.append((r-1)%n)
                break
            if arr:
                d=arr[0]
                if d==(l-1)%n:
                    arr.pop(0)
            if len(arr)==0:
                res +=1
            r +=1
        return res
