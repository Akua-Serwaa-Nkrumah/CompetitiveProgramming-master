def BinDeq(a):
    a_sum = [a[0]]*n
    for i in range(1,n):
        a_sum[i] = a_sum[i-1] + a[i]
    
    l, r = 0, 0
    total = a_sum[-1]
    mx = 0
    
    if total == s:
        return 0
    
    if total < s:
        return -1
    
    total = 0
    
    while r < n:
        total += a[r]
        
        if total > s:
            total -= a[l]
            l += 1

        if total == s: 
            mx = max(mx,r-l+1)
            
        r += 1
        
    return (n-mx)


t = int(input())
for _ in range(t):
    n, s = map(int,input().split())
    a = list(map(int,input().split()))
    print(BinDeq(a))
    