t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    b = [a[0]]*n

    for i in range(1,n):
        b[i] = (b[i-1] + a[i]) 
    for i in range(1,n):
        if b[i]%2 == 1:
            b[i] -= 1
        if b[i] == b[i-1]:
            b[i-1] -= 2

    print(*b)
