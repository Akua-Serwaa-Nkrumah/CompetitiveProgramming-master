def solve(a,b,n):
    
    if n == 1 and a[0] < b[0]:
        return 'NO'
    
    for i in range(1,n):
        if b[0] != 0:
            if (a[i] - b[i]) > (a[0] - b[0]) or (a[i] < b[i]):
                return 'NO'
            
        else: 
            if (a[i] - b[i]) > a[0]:
                return 'NO'
   
    return 'YES'
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    print(solve(a,b,n))