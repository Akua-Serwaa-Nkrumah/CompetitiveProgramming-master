def GoodPair():
    n = int(input())  
    a = list(map(int, input().split()))
    max_position = a.index(max(a))+1
    min_position = a.index(min(a))+1
    print(min(max_position,min_position),max(min_position,max_position))
    return
t = int(input())  
for _ in range(t):
    GoodPair()
    