t = int(input())
for _ in range(t):
    n, q = map(int, input().split())

    a = []

    for i in range(n):
        b, x = map(int, input().split())

        if b == 1:
            a.append(x)
        else:
            prev = a[:]
            for i in range(min(x,10**8//len(a))):
                if len(a) <= 10**8:
                    a += prev

    queries = list(map(int, input().split()))

    res = []

    for i in queries:
        i = min(i, len(a))
        res.append(a[i-1])

    print(res)
