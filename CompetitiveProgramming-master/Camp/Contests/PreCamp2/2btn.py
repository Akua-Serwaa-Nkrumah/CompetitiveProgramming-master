def Greater(n,m,ans):
    while m > n:
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
        ans += 1
        
    ans += n - m
    return ans 

n, m = map(int,input().split())
if m <= n:
    print(n-m)
else:
    ans = 0
    print(Greater(n,m,ans))



