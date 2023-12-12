def DoraSearch(a,n):
    
    left, right = 0 , n-1
    minimum, maximum = 1, n

    while left < right:
        if (a[left] != maximum) and (a[left] != minimum) and (a[right] != maximum) and (a[right] != minimum):
            return(left+1, right+1)
            
        elif (a[left] == maximum):
            left += 1
            maximum -= 1
            
        elif (a[left] == minimum):
            left += 1
            minimum += 1
            
        elif (a[right] == maximum):
            right -= 1
            maximum -=1
        elif (a[right] == minimum):
            right -= 1
            minimum += 1
    return -1
            
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if DoraSearch(a,n) != -1:
        print(*DoraSearch(a,n))
    else :
        print(-1)

        
    
        
    