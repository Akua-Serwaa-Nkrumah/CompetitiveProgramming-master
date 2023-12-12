def Desort(a):
    if sorted(a) != a:
        return 0
    
    dif = [a[-1]]*n
    
    for i in range(n-2,-1,-1):
        dif[i] = a[i+1] - a[i]
    
    return (min(dif)//2) + 1

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    print(Desort(a))
    
