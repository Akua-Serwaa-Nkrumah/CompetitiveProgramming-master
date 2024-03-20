t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    mx = 0

    l,r = 0,0
    while l <=r and r < n:
        if a[r] != 0:
            mx = max(mx,r-l)
            l = r+1
        r += 1

    mx = max(mx,r-l)
    print(mx)