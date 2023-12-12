n, k = map(int,input().split())
h = list(map(int,input().split()))

l = 0

total = sum(h[l:k])
mn = total
index = 0

for r in range(k,n):
    total = total + h[r] - h[l]

    l += 1
    if total < mn:
        index = l
        mn = total
        
        
print(index+1)
        
        
    