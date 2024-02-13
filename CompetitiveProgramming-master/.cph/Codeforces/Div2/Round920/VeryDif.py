t = int(input())

for _ in range(t):
    n,m = map(int,input().split())

    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())), reverse= True)

    
    total = 0
    i, j = 0, m-1
    while j - i > m- n:
        total += abs(b[i] - a[i]) + abs(b[j] - a[j-(m-n)])
        i += 1
        j -= 1

    print(total)
