from math import sqrt

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)

    if sqrt(total) == int(sqrt(total)):
        print("YES")
    else:
        print("NO")

