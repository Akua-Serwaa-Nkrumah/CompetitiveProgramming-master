def ShiftStacks(n,h):
    extra = 0
    for i in range(n):
        if h[i] >= i:
            extra += (h[i]-i)
            
        elif h[i]+extra >= i:
            extra -= (i-h[i])
            
        else: 
            return "NO"
        
    return "YES"
        

t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int,input().split()))
    print(ShiftStacks(n,h))
    
    
    