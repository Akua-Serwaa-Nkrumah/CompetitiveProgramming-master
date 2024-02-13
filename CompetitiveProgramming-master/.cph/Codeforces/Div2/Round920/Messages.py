def solve():
    n,f,x,b= map(int,input().split())
    a = [0]+list(map(int,input().split()))
    a.sort()
    down = f
    for i in range(1,n+1):
        choice = min((a[i]-a[i-1])*x,b)
        down -= choice
        if down <= 0:
            return "NO"
    return "YES" 


t = int(input())
for _ in range(t):
    print(solve())