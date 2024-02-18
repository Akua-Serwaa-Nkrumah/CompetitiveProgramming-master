t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int,input().split()))

    m = int(input())
    b = list(map(int,input().split()))

    a = []

    for i in range(min(n,m)):
        if r[i] > b[i]:
            a.append(r[i])
            a.append(b[i])

        else:
            a.append(b[i])
            a.append(r[i])

    if n > m:
        a.extend(r[m:])
    else:
        a.extend(b[n:])

 
    for i in range(1,n+m):
        a[i] += a[i-1]

    print(max(0,max(a)))
