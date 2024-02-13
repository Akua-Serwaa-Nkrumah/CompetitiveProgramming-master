t = int(input())
for _ in range(t):
    a,b = map(int,input().split())

    if a == 0:
        print('Bob')
    elif b == 0:
        print('Alice')
    else:
        if abs(a-b)%2 == 0:
            print('Bob')
        else:
            print('Alice')