def Favorite(arr, n):
    pre, last = 0 , n-1
    
    fav = []
    while pre <= last: 
        fav.append(arr[pre])
        if pre != last:
            fav.append(arr[last])
        pre += 1
        last -= 1
        
    return fav

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    print(*Favorite(array,n))