def RemoveSmallest(arr):
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) > 1:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(RemoveSmallest(arr))