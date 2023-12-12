def check(mid):
    count = 0
    for i in range(n-1):
        if a[i+1] - a[i] >= mid:
            count += mid
        else: 
            count += a[i+1] - a[i] 
            
    count += mid
    return count
    
def BinSearch(h):
    l, r = 1, h
    while l <= r:
        mid = l + (r-l)//2
        
        if check(mid) >= h:
            r = mid - 1
        else: 
            l = mid + 1
            
    return l
    
       
t = int(input())
for _ in range(t):
    n, h = map(int,input().split())
    a = list(map(int,input().split()))
    print(BinSearch(h))
    
        
    
        