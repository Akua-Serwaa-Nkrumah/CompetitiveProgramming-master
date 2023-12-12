def Cards(a,b):
    
    if (a[-1] > b[-1]):
        print("Alice")
        print("Alice")
        
    elif (b[-1] > a[-1]):
        print("Bob")
        print("Bob")
    
    else: 
        print('Alice')
        print('Bob')
        
    return

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int,input().split())))
    m = int(input())
    b = sorted(list(map(int,input().split())))
    Cards(a,b)