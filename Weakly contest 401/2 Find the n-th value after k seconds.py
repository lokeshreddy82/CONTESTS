class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        arr=[1 for i in range(n)]
        modd=(10**9)+7
        for j in range(k):
            for i in range(1,n):
                arr[i]=(arr[i]+arr[i-1])%modd
            
        return arr[n-1]%modd
