def increase(a):
    
    if len(set(a)) == n:
        return "YES"
    
    return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(increase(a))