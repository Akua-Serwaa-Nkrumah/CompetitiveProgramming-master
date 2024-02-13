t = int(input())
for _ in range(t):
    b = list(map(int,input().split()))

    a = b[:3]

    print(*a)
