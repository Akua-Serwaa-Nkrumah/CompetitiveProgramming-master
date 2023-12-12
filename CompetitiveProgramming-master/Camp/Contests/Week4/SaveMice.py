t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x = sorted(list(map(int, input().split())))
    
    cat, hole = 0, n
    count = 0
    l = 0
    pointer = len(x) - 1
    
    
    while cat < x[pointer] and pointer >= 0:
        diff = n - x[pointer]
        if x[pointer] == n:
            count += 1
            pointer -= 1
        else: 
            x[pointer] += diff
            cat += diff
            if cat == x[l]:
                l += 1
            
    print(count)