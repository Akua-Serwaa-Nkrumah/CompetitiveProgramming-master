t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int,input().split()))

    i = 0
    while i < n and a[i] == 0:
        i += 1

    zero, total = 0, 0
    
    if i == n:
        print(total)
    else:
        for j in range(i,n-1):
            if a[j] == 0:
                zero += 1

            total += a[j]

        print(total + zero)
            