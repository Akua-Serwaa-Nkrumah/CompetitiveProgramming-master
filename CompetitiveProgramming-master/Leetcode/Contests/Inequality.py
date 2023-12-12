def Inqeuality(n,a):
    count = 0
    l, r = 0, 1 
    
    while l < r < n:
        if a[l] < l+1 < a[r] < a[r+1]:
            count += 1
            r += 1
        elif a[l] >= l + 1:
            l += 1
        if l == r: 
            r += 1
                
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(Inqeuality(n,a))