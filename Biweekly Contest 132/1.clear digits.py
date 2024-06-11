class Solution:
    def clearDigits(self, s: str) -> str:
        k=[]
        for i in range(len(s)):
            if s[i].isdigit():
                k.pop()
            else:
                k.append(s[i])
        return "".join(k)
