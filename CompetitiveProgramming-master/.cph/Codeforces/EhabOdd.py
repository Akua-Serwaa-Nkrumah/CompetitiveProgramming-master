def Odd():
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n):
        for j in range(n):
            if (a[i]+a[j])%2 == 1 and a[i]>a[j]:
                a[i],a[j] = a[j],a[i]
            if all(a[i] <= a[i+1] for i in range(n-1)):
                print(*a)
                return
            
Odd()

