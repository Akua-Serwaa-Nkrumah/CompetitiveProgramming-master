t = int(input())

for _ in range(t):
    n = int(input())

    p = list(map(int,input().split()))
    q = input()
    ans = []
    l,r = 0, n-1

    ranges = list(range(1,n+1))

    for i in range(n):  
        if q[i] == '0':
            ans.append(ranges[l])
            l += 1
        else:
            ans.append(ranges[r])
            r -= 1


    print(*ans)

