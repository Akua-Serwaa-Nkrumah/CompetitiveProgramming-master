def Strongest():
    n = int(input())
    s = list(map(int,input().split()))
    compare = sorted(s[:])
    strength_dif = []
    for i in range(n):
        if s[i] != compare[-1]:
            strength_dif.append(s[i]-compare[-1])
        else: 
            strength_dif.append(s[i]-compare[-2])
    print(*strength_dif)
    
t = int(input())
for _ in range(t):
    Strongest()
    
    
