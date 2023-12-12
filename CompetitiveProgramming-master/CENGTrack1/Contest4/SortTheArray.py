def sortArr(a):
    start, end = -1, -1

    i ,j = 0,n-1
    
    for i in range(n-1):
        if a[i] > a[i+1]:
            start = i
            break
       
    for j in range(n-1,0,-1):
        if a[j] < a[j-1]:
            end = j
            break
    
    if start >= end:
        print("yes")
        print(1,1)
        return
    
    if a[:start] + a[start:end+1][::-1] + a[end+1:] == sorted(a):
        print("yes")
        print (start+1, end+1, sep = ' ')
        return
    
    print ("no")
    return


n = int(input())
a= list(map(int, input().split()))

sortArr(a)
