t = int(input())
for _ in range(t):
    res = sorted(map(int,input().split()))
    if res[0] + res[1] < 4 or res[0] == 0 or res[1] == 0:
        print(0)
        
    else: 
        count = 0
        if  res[0] + res[1] < 8:
            print (1)
        
        elif res[0] < 4:
            print(res[0])
        else: 
            print(res[0]//2)
        