t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    for i in range(1,n-1):
        if b[i] == a[i-1]:
            a[i+1] = 0
        else:
            a[i+1] = b[i]
    print(*a)
 
    