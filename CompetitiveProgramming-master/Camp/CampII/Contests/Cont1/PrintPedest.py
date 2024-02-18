t = int(input())

for _ in range(t):
    n = int(input())
    a = [n-(n//2)-1,n//2,1]
    if a[0] == a[1]:
        a[0] -=1
        a[1] += 1

    print(*a) 