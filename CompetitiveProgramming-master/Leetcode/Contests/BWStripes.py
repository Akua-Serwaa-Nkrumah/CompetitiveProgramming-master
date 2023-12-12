t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    l = 0
    white = 0
    
    ans = float('inf')
    for r in range(n):
        if s[r] == 'W':
            white += 1
            
        if r-l+1 == k:
            ans = min(ans, white)
            
            if s[l] == 'W':
                white -= 1
                
            l += 1
        
    print(ans)
            
    