t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int,input().split()))
    
    for i in range(2,n-1):
        if a[i] >= a[i-2]:
            a[i] -= a[i-2]
            a[i-1] = 0

        else:
            print('NO')
            break

    if a[-1] == a[-2] == 0:
        print('YES')
    else:
        print('NO')