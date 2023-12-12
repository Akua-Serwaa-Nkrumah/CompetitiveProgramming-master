n = int(input())
a = list(map(int,input().split()))

cost = 0
zero = 0
neg = 0

for num in a:
    if num == 0:
        zero += 1
        cost += 1
    elif num < 0:
        neg += 1
        cost += (-1-num)
    else: 
        cost += (num-1)
        
if neg%2 == 0 :
    print(cost)
elif (neg%2 == 1 and zero != 0):
    print(cost)
else: 
    print(cost+2)
    

    
