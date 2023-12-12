t = int(input())
for _ in range(t):
    a = input()
    
    l, r = 0, 5
    
    left, right = 0, 0
    
    while l < r:
        left += int(a[l])
        right += int(a[r])
    
        l += 1
        r -= 1
        
    
    if left == right:
        print("YES")
        
    else: 
        print("NO")
        