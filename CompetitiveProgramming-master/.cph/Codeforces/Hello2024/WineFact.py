n, q = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

for _ in range(q):
    p,x,y,z = map(int,input().split())
    total = 0
    if b[0] <= a[0]:
        total += b[0]
    a[p-1] = x
    b[p-1] = y
    c[p-2] = z
    

    prev_a = a[:]
    prev_b = b[:]
    prev_c = c[:]
    for i in range(1,n):
        if a[i-1] > b[i-1]:
            a[i] += a[i-1] - b[i-1]

            if b[i] <= a[i]:
                total += b[i]
            else: 
                total += a[i]

    a[p-1] = x
    b[p-1] = y
    c[p-2] = z
    a = prev_a
    b = prev_b

    print(total)
