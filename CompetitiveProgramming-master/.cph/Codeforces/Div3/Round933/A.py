t = int(input())

for _ in range(t):
    n,m,k = map(int,input().split())

    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    cnt = 0

    for i in range(n):
        for j in range(m):
            if b[i] + c[j] <= k:
                cnt += 1 

    print(cnt)