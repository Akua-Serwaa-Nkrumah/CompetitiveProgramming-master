t = int(input())
for _ in range(t):
    x,y,k = map(int,input().split())
    if x >= y:
        print(x)
        
    else: 
        if k >= (y-x):
            print(y)
        else:
            print(y + y - (x+k))