from collections import defaultdict

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())

    k = list(map(int,input().split()))
    c = list(map(int,input().split()))
    c = [0] + c
    dic = defaultdict(int)
    cst = 0

    for i in range(n):
        min(min(c[1:k[i]+1]),c[k[i]])
    print(cst)