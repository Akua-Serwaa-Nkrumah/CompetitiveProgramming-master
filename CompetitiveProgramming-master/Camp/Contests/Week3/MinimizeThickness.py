def Thickness(a,n):
    if total/n != int(total/n):
        return n   
    count = 0
    l, r = 0, 0
    
    while r < n: 
        if sum(a[l:r+1]) == max_element:
            l = r + 1
            count = max(count)
            
        elif sum(a[l:r+1]) < max_element:
            r+= 1
            
        else:
            count += 1
            l = r
            
    return count

t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    max_element = max(a)
    print(Thickness(a,n))
    
