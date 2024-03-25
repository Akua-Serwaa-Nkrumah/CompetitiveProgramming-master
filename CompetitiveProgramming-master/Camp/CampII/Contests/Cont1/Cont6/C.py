t = int(input())
for _ in range(t):
    n,m = map(int,input().split())

    k = list(map(int,input().split()))
    c = list(map(int,input().split()))
    
    cst = 0
    k.sort(reverse= True)

    i,j = 0, 0
    
    while j < m and i < n:
        if c[j] > c[k[i]-1]:
            cst += c[k[i]-1]
            
        else:
            cst += c[j]
            j += 1

        i += 1

    while i < n:
        cst += c[k[i]-1]
        i += 1

    print(cst)