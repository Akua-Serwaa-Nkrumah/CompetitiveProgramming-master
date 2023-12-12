n = int(input())
a = list(map(int,input().split()))
count = 1
max_length = 0

if len(a) == 1:
    print(1)
else: 
    for i in range(n-1):
        if a[i+1] > a[i]:
            count += 1   
        else: 
            count = 1
            
        max_length= max(max_length,count)
    

    print(max_length)