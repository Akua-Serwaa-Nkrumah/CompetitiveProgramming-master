t = int(input())

for _ in range(t):
    
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse= True)

    count = 0
    for i in range(n-1):
        count += (a[i] -a[i+1])


    print(count)