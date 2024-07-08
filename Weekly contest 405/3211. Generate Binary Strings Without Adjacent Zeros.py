class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.res=[]
        def dfs(string,ind):
            if ind==0:
                self.res.append(string)
                return
            if string[-1]=="0":
                dfs(string+"1",ind-1)
            else:
                dfs(string+"0",ind-1)
                dfs(string+"1",ind-1)                
            return
        dfs("0",n-1)
        dfs("1",n-1)
        return self.res
