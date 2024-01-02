t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    b = list(map(int,input().split()))

    total = 1
    for i in b:
        total *= i
    
    if 2023/total != int(2023/total):
        print("NO")
    else:
        print('YES')
        ans = [2023//total]
        for i in range(k-1):
            ans.append(1)
        print(*ans)

