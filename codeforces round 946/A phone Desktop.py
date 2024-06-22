import math
for i in range(int(input(""))):
    x,y=map(int,input().split())
    if x==0 and y==0:
        print(0)
    else:
        counting=0
        cells=y//2+y%2
        counting=counting+4 if y%2!=0 else 0
        counting=x-(counting+(cells*7))
        if counting<=0:
            print(cells)
        else:
            cells +=math.ceil(counting/15)
            print(cells)
