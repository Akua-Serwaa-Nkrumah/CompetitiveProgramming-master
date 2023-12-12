def Blanks(a):
    r = 0
    count = 0
    mx = 0
    while r < n:
        if a[r] == 0:
            count += 1
        else: 
            mx = max(mx,count)
            count = 0
        
        r += 1 
        
    mx = max(mx,count) 
    return mx

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(Blanks(a))