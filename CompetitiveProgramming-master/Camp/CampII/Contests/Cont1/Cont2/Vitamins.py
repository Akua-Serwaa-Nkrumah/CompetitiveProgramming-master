from collections import defaultdict

n = int(input())
vit = defaultdict(int)
for _ in range(n):
    c, vitamin = input().split()
    vitamin = ''.join(sorted(vitamin))
    
    if vit[vitamin] != 0:
        vit[vitamin] = min(vit[vitamin],int(c))
    else:
        vit[vitamin] = int(c)

print(vit)

