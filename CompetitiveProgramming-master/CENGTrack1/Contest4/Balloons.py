from collections import Counter

def Balloon(s):
    
    s_count = Counter(s)
    total = 2*len(s_count)
    for a in s_count:
        if s_count[a] > 1:
            total += (s_count[a] -1)
    
    return total

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(Balloon(s))