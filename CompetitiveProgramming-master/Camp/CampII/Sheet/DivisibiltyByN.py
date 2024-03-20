def two_in_arr(n):
    cnt = 0

    while n % 2 == 0:
        n = n//2
        cnt += 1

    return cnt

t= int(input())
for _ in range(t):
    n = int(input())

    a = list(map(int,input().split()))

    in_arr = 0
    in_idx = []

    for i in range(n):
        in_arr += two_in_arr(a[i])

        if (i+1)%2 == 0:
            in_idx.append(two_in_arr(i+1))

    in_idx.sort(reverse= True)
    cnt = 0

    if in_arr >= n:
        print(0)

    else:
        cnt += in_arr
        i = 0
        while cnt < n and i < len(in_idx):
            cnt += in_idx[i]
            i += 1

        if cnt >= n:
            print(i)
        else:
            print(-1)