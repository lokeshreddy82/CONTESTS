for _ in range(int(input(""))):
    n,k=map(int,input().split())
    res=0
    while n:
        res +=1
        n-=1
        if n==0:
            break
        else:
            res +=k-1
    print(res)
