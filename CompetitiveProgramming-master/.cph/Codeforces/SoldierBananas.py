k, n , w = map(int,input().split())
# print(k,n,w)
cost = 0

for i in range(1,w+1):
    cost += i*k

if cost > n:
    print(cost-n)
else: 
    print(0)
    
        
    