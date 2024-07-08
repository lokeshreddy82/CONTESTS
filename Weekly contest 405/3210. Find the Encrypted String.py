class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        l=list(s)
        n=len(s)
        for i in range(len(s)):
            r=(i+k)%n
            l[i]=s[r]
        return "".join(l)
