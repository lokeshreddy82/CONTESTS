#BIT MANIPUTLATION
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k =1
    for i in range(20):
        one_p = 0
        for j in range(n):
            if(arr[j]&(1<<i)):
                k = max(k, j+1-one_p)
                one_p = j+1
        if(one_p != 0):
            k = max(k, n+1-one_p)
    print(k)