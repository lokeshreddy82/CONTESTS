for _ in range(int(input(""))):
     n=int(input(""))
     res=0
     heights=list(map(int,input().split()))
     def can_all_flowers_become_zero(T, heights):
        n = len(heights)
        current_heights = heights[:]
        
        for i in range(n - 1):
            current_heights[i] = max(0, current_heights[i] - (T - i))
            if current_heights[i] > current_heights[i + 1]:
                return False
        
        current_heights[n - 1] = max(0, current_heights[n - 1] - T + (n - 1))
        return all(h == 0 for h in current_heights)
     low=1
     high=sum(heights)
     answer=high
     while low < high:
          mid = (low + high) // 2
          if can_all_flowers_become_zero(mid, heights):
               answer = mid
               high = mid
          else:
               low = mid + 1
     print(answer)