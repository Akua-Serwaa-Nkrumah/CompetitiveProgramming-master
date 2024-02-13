t = int(input())
for _ in range(t):
    n = int(input())

    a = list(map(int,input().split()))

    i, j = 0, n-1

    while i < n-1 and a[i] == a[i+1]:
        i += 1

    while j > 0 and a[j] == a[j-1]:
        j -= 1

    if a[i] == a[j]:
        print(max(0,j - i -1))
    else:
        mx = max(i,n-j-1)
        print(n-mx-1)
