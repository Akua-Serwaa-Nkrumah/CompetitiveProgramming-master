t = int(input())

for _ in range(t):
    a,b = map(int,input().split())

    c = a*b
    for i in range(min(a,b),c**2 + 1):
        if (i != b and i != a) and i%a == 0 and i%b == 0:
            print(i)
            break