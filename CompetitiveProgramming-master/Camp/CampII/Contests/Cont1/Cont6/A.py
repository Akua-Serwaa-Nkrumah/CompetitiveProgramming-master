t = int(input())

for _ in range(t):
    a = list(map(int,input().split()))
    a.sort()
    if a[0] + a[1] == a[2]:
        print('YES')
    else:
        print('NO')