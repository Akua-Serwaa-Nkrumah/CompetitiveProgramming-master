def Beautiful(a,b,c,d):
    if (a < b and c < d and a < c and b < d) or (c < a and d < b and c < d and a < b) or (d < c and b < a and d < b and c < a) or (b < d and a < c and b < a and d < c):
        return True
    
    return False


t  = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    if Beautiful(a,b,c,d):
        print ("YES")
    else: 
        print("NO")