n = int(input())
a = list(map(int,input().split()))

r = 0
max_length = 0
count = 1

while r < n-1:
    if a[r] <= a[r+1]:
        count += 1
        
    else: 
        max_length = max(max_length, count)
        count = 1
    r += 1 
    
max_length = max(max_length, count)

print(max_length)
    