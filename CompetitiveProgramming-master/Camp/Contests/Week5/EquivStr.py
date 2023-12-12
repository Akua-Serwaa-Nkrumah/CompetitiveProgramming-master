a = input()
b = input()

equiv =  dict()

def Check(a,b):
    
    if len(a)%2 == 1:
        return a == b
    
    if (a,b) in equiv:
        return equiv[a,b]
    
    a1 = a[:len(a)//2]
    a2 = a[len(a)//2:]
    
    b1 = b[:len(b)//2]
    b2 = b[len(b)//2:]
    
    equiv[a,b] = Check(a1,b1) and Check(a2,b2) or Check(a1,b2) and Check(a2,b1)
        
    return equiv[a,b]

if Check(a,b): print('YES')
else: print('NO')