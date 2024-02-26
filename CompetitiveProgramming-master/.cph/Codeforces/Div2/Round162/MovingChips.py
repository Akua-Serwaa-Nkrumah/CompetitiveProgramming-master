t = int(input())
for _ in range(t):
    n = int(input())

    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] == 1:
            l = i
            break

    r = l+1
    cnt = 0
    res = 0
    while l < r and r < n:
        if a[r] == 0:
            cnt += 1

        else:
            res += cnt
            cnt = 0
            l = r
        r += 1

    print(res)

