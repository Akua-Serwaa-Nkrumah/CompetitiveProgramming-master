def Tree(p):
    res = 0
    i = 2
    while i < m:
        for i in range(0,m-1,2):
            if abs(p[i]-p[i+1]) > 1:
                return -1
        
        
            
    for i in range():
        continue
    
    return res

def Divide(p):
    if len(p) == 1:
        return
    
    p1 = p[:len(p)//2]   
    p2 = p[len(p)//2:] 
    
    
    
    Divide(p1)
    Divide(p2)
      
      
    
    return 
t = int(input())
for _ in range(t):
    m = int(input())
    p = list(map(int,input().split()))
    print(Tree(p))