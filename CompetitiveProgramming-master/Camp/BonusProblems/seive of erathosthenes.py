from math import ceil

arr = [1]*(1000000)
arr[0] = arr[1] = 0

for i in range(2,1001):
    if arr[i] == 1:
        for j in range(i**2,1001,i):
            arr[j] = 0

print(arr[0:11])
        