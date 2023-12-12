
n, q = map(int,input().split())

p = sorted(list(map(int,input().split())))

result = [p[0]]*(n)

for i in range(1,n):
    result[i] = result[i-1]+p[i]


for _ in range(q):
    x, y = map(int,input().split())
    
    print (result[n-(x-y)-1] - result[n-x-1] if x!=n else result[y-1])




    
    