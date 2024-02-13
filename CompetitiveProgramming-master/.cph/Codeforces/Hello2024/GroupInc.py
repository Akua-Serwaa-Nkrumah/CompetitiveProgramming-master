t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    test = 0
    for i in range(n-1):
        if a[i] < a[i+1]:
            test += 1

    if test > 0:
        print(test -1)
    else:
        print(0)