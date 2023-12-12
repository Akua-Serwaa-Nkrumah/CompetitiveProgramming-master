t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int,input().split()))
    
    m = int(input())
    b = list(map(int, input().split()))
    
    a = []
    if n > m: 
        for i in range(m):
            a.append(r[i])
            a.append(b[i])
            
        for i in range(m,n):
            a.append(r[i])
            
    else: 
        for i in range(n):
            a.append(b[i])
            a.append(r[i])
            
        for i in range(n,m):
            a.append(b[i])

    a_sum = [a[0]]*(n+m)

    for i in range(1,n+m):
        a_sum[i] = a_sum[i-1]+a[i]
        
    print (max(0,max(a_sum)))

    
