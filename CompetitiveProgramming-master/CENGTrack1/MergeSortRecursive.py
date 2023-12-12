def merge(a,b):
    a_ptr, b_ptr = 0, 0
    res = []
    while a_ptr < len(a) and b_ptr < len(b) : 
        if a[a_ptr] < b[b_ptr]:
            res.append(a[a_ptr])
            a_ptr += 1
        else: 
            res.append(b[b_ptr])
            b_ptr += 1
            
    if a_ptr == len(a):
        while b_ptr < len(b):
            res.append(b[b_ptr])
            b_ptr += 1
            
    elif b_ptr == len(b):
         while a_ptr < len(a):
            res.append(a[a_ptr])
            a_ptr += 1
            
    return res

def merge_sort(c):
    if len(c) == 1:
        return c
    
    a = merge_sort(c[:len(c)//2])
    b = merge_sort(c[len(c)//2:])
    print(a,b)
    return merge(a,b)
    
    
print(merge_sort([5,5,6,2,8,9,10]))
    
    