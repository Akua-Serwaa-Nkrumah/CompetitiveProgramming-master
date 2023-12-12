def Valley(arr):
        min_element = min(arr)
        min_position = arr.index(min_element)
        # print (min_element, min_position)
    
        for i in range(min_position):
            if arr[i] < arr[i+1]:
                return False
        for  j in range(min_position,len(arr)-1):
            if arr[j] > arr[j+1]:
                return False
    
        return True
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if Valley(arr):
        print("YES")
    else: 
        print("NO")