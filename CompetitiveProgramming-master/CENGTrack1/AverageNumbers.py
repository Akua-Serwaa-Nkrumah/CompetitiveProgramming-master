n = int(input())
arr = list(map(int,input().split()))
average = sum(arr)/len(arr)
if average in arr:
    print(arr.count(average))
    position = []
    for i in range(len(arr)):
        if arr[i] == average:
            position.append(i+1)
    print(*position)
else: 
    print(0)
    