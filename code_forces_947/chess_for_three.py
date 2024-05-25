n=int(input())
for i in range(n):
     p1,p2,p3=map(int,input().split())
     if (p1+p2+p3)%2==1:
          print(-1)
     else:
          p2 +=p1
          if p2>p3:
               print((p2+p3)//2)
          else:
               print(p2)