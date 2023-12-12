def LessOrEqual():
    n, k = map(int,input().split())
    numbers = sorted(map(int,input().split()))
    check = []
    
    if k == 0:
        return numbers[0] - 1 if numbers[0] > 1 else -1
    
    if k > len(numbers):
        return -1
    
    for i in range(k):
        check.append(numbers[i])
        numbers[i] = -1
    
    for number in numbers[k:]:
        if number == check[-1]:
            return -1
        
    return check[-1]
    
print(LessOrEqual())  
