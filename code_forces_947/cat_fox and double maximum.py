"""def solve():
  n = int(input())
  a = [int(x) for x in input().split(" ")]
  ans = [0 for _ in range(n)]
  pos = [0 for _ in range(n+1)]
  for i in range(n):
    ans[i] = n+1-a[i]
    pos[a[i]] = i
  for i in range(1, n+1):
    if (pos[i]&1) != (pos[1]&1):
      ans[pos[i]], ans[pos[1]] = ans[pos[1]], ans[pos[i]]
  print(*ans)
for _ in range(int(input())):
  solve()
"""
for t in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    odds = []
    evens = []
    for i in range(n):
        if i % 2:
            odds.append((p[i],i))
        else:
            evens.append((p[i],i))

    odds.sort()
    evens.sort()
    print(odds,evens)
    if evens[0][0] == 1:
        odds,evens = evens,odds
    ans = [0]*n
    print(odds,evens)
    # print('odds:',odds,evens)
    for i in range(n//2):
        ans[odds[i][1]] = n//2 - i
        ans[evens[i][1]] = n - i
    ans = [str(i) for i in ans]
    print(' '.join(ans))
    