def PairWiseDistance():
    a,b,c = map(int,input().split())
    min_distance = abs(a-b) + abs(b-c) + abs(a-c) - 4
    min_distance = max(0,min_distance)
    return min_distance

t = int(input())
for _ in range(t):
    print(PairWiseDistance())