def Triple(a,n):
    left, right = 0, 1
    count = 1
    
    while right < n:
        if a[left] == a[right]:
            count += 1
            
        else:
            count = 1
            left = right
            
        if count == 3:
            return a[left]
        
        right += 1
        
    return -1
    
t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print(Triple(a,n))
    
    