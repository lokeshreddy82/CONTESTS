class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        hashing={}
        for i  in range(len(skills)):
            hashing[skills[i]]=i
        queue=[skills[0],skills[1]]
        max_element=-1
        arr=2
        countt={}
        enter=2
        n=len(skills)
        if n==2:
            return hashing.get(max(skills))
        while queue:
            if queue[0]>queue[1]:
                countt[queue[0]]=countt.get(queue[0],0)+1
                if countt[queue[0]]==k:
                    return hashing.get(queue[0])
                queue[1]=skills[enter]
            else:
                countt[queue[1]]=countt.get(queue[1],0)+1
                if countt[queue[1]]==k:
                    return hashing.get(queue[1])
                queue[0]=skills[enter]
            enter +=1
            max_element=max(max_element,max(queue))
            if enter==n:
                break
        return hashing.get(max_element)
        
            
                
                
                
