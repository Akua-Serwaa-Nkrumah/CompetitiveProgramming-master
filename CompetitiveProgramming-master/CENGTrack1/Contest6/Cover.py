def solve():
    if len(set(s)) == 1:
        if s[0] == '#':
            return 0
        
        else: 
            if n < 3:
                return n
            
            return 3
        
    for i in range(n):
        if s[i] == '#':
            s[i] = 0
        else:
            s[i] = 1
            
    s_sum = [s[i]]*n
    
    for i in range(1,n):
        s_sum[i] = s_sum[i-1] + s[i]
    
    l, r = 0, 0
    
    total = 0
    
    while r < n:
        if s_sum[r] >= s_sum[l]:
            if r - l >= 3:
                total += (r-l)
                break
            else: 
                
                
             l = r
                
        r += 1
    
    return total

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    print(solve())
