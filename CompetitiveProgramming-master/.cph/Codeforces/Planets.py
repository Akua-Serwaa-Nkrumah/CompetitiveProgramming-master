from collections import Counter

t = int(input())  
for _ in range(t):
    n, c = map(int, input().split())  
    a = list(map(int,input().split()))
    planets = Counter(a)
    
    total = 0
    
    for orbit in planets:
        if c <= planets[orbit]:
            total += c   
        else: 
            total += planets[orbit]

    print(total)
    
