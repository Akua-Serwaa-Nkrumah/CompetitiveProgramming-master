n = int(input())
t = list(map(int,input().split()))
        
def Choco(n,t):
    a_c, b_c = 0, 0
    Al, Bb = 0, 0
    l , r = 0, n -1
    
    while l <= r:
        if Al <= Bb: 
            a_c += 1
            Al += t[l]
            l += 1
        else: 
            b_c += 1
            Bb += t[r]
            r -= 1
    
        
    return (a_c,b_c)
    
print(*Choco(n,t))