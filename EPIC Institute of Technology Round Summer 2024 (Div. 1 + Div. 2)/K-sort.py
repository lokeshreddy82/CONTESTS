for _ in range(int(input(""))):
    res=0
    import heapq
    n=int(input(""))
    a=list(map(int,input().split()))
    nedded_array=[]
    for i in range(1,n):
        if a[i-1]>a[i]:
            nedded_array.append(a[i-1]-a[i])
            a[i]=a[i-1]
    decrease=0
    res=0
    nedded_array.sort(reverse=True)
    while nedded_array:
        k=len(nedded_array)
        minimum=nedded_array[-1]-decrease
        decrease +=minimum
        res +=minimum*k+minimum
        nedded_array.pop()
    print(res)