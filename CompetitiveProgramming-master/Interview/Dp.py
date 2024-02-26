def solution(first,second, target):
    def dp(i, sum_):
        if i > len(arr):
            if sum_ == target:
                res += 1
            return
    
        l = dp(i+1, sum_ + arr[i][0])
        r = dp(i+1, sum_)
        
    res = 0
    arr = []
    for i in range(len(first)):
        arr.append((first[i], 0))

    for i in range(len(second)):
        arr.append((second[i], 1))
    dp(0, 0)
    return res