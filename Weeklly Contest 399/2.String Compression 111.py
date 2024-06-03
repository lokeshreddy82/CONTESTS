class Solution:
    def compressedString(self, word: str) -> str:
        res=""
        countt=1
        carry=word[0]
        word +="?"
        for i in range(1,len(word)):
            if carry==word[i]:
                countt +=1
                if countt==9:
                    res +=str(countt)+carry
                    countt=0
            elif carry!=word[i]:
                if countt!=0:
                    res +=str(countt)+carry
                carry=word[i]
                countt=1
        return res
                
            