class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        value=0
        flag=True
        for i in range(k):
            if flag:
                value +=1
                if value==n-1:
                    flag=False
            else:
                value -=1
                if value==0:
                    flag=True
        return value
