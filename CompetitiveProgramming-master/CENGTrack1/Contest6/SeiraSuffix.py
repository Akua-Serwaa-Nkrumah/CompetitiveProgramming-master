n, m = map(int,input().split())
a = list(map(int,input().split()))

a_set = set()
l = [0]*n

for i in range(n-1,-1,-1):
    a_set.add(a[i])
    l[i] = len(a_set)
    
    
for _ in range(m):
    idx = int(input())
    print(l[idx-1])