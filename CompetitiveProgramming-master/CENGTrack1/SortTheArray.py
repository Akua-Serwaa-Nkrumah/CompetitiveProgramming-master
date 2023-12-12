def sortArraySegment(n, arr):
    start = -1
    end = -1

    i = 0
    j = n-1
    
    while i < n-1 and arr[i] < arr[i+1] :
        i += 1
        
    start = i
    
    while j > 0 and arr[j] > arr[j-1]:
        j -= 1
            
    end = j
    
    if start > end:
        print("yes")
        print(1,1)
        return
    
    if arr[:start] + arr[start:end+1][::-1] + arr[end+1:] == sorted(arr):
        print("yes")
        print (start+1, end+1, sep = ' ')
        return
    
    print ("no")
    return


n = int(input())
arr = list(map(int, input().split()))

sortArraySegment(n, arr)
