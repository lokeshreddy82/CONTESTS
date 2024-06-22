for _ in range(int(input())):
    input()
    s = input()
    a = sorted(set(s))
    d = {a[i]: a[-1 - i] for i in range(len(a))}
    print(*map(d.get, s), sep="")
