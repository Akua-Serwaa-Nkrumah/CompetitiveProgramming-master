t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    mx = max(a)

    res = 0
    for i in a:
        res = max(res,abs(mx-i))

    print(res)