import math
 
def is_perfect_square(n):
    return math.sqrt(n)**2 == n

m = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
j = 0
while j < len(arr):
    if arr[j] < 0:
        j+=1
        continue
    if is_perfect_square(arr[j]) == True:
        arr.remove(arr[j])
    else:
        j+= 1
print(max(arr))
    
