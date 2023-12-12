def Candies(n,w):
    w_prefix = [w[0]]*n
    w_suffix = [w[-1]]*n
    l, r = 0, n-1
    res = []
    for i in range(1,n):
        w_prefix[i] = w_prefix[i-1] + w[i]
        
    for j in range(n-2,-1,-1):
        w_suffix[j] = w_suffix[j+1] + w[j]
        
    while l < r:
        if w_prefix[l] == w_suffix[r]:
            res.append(n- r + l + 1)
            l += 1
            r -= 1
            
        elif w_prefix[l] < w_suffix[r]:
            l += 1
            
        else: 
            r -= 1
    
    return res[-1] if res else 0
    

t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int,input().split()))
    
    print(Candies(n,w))