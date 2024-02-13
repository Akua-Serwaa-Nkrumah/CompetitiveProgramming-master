n,m,s,A,B = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a = sorted(a)
b = sorted(b)

total, mx_val = 0, 0
a_ptr, b_ptr = n-1, m-1

while total < s and b_ptr >= 0 and a_ptr >= 0:
    
    if a[a_ptr] > b[b_ptr]:
        total += A
        mx_val += a[a_ptr]
        if total > s:
            mx_val -= a[a_ptr]
        a_ptr -= 1
        
    elif a[a_ptr] < b[b_ptr]:
        total += B
        mx_val += b[b_ptr]
        if total > s:
            mx_val -= b[b_ptr]
        b_ptr -= 1
        
    else:
        if A < B:
            total += A
            mx_val += a[a_ptr]
            if total > s:
                mx_val -= a[a_ptr]
            a_ptr -= 1
        else:
            total += B
            mx_val += b[b_ptr]
            if total > s:
                mx_val -= b[b_ptr]
            b_ptr -= 1

print(mx_val)