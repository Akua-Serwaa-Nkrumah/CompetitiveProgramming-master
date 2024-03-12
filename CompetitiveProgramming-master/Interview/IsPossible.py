def dp(x,y,c,d):
    if x == c and y == d:
        return True
    
    if x > c or y > d:
        return False
    
    return dp(x+y,y,c,d) or dp(x,x+y,c,d)

if dp(4,3,5,4):
    print('YES')

else:
    print('NO')

memo = {'Jan':'01','Feb':'02'}