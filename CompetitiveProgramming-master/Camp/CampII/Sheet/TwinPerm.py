t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    res = []

    mx = max(a)

    for i in range(n):
        res.append(mx-a[i]+1)

    print(*res)