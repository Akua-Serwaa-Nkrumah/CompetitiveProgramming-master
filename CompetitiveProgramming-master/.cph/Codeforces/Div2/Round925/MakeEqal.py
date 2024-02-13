t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    total = sum(a)

    equal = total//n

    for i in range(n-1,0,-1):
        if a[i] < equal:
            rem = equal - a[i]
            a[i] += rem
            a[i-1] -= rem

    # print(a)
    if len(set(a)) == 1:
        print('YES')
    else:
        print('NO')