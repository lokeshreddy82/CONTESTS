for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b={}
    col=0
    for i in range(n-2):
        g=[(0,a[i+1],a[i+2]),(a[i],0,a[i+2]),(a[i],a[i+1],0)]
        t=(a[i],a[i+1],a[i+2])
        for j in g:
            col+=b.get(j,0)-b.get(t,0)
            b[j]=b.get(j,0)+1
        b[t]=b.get(t,0)+1
    print(col)
