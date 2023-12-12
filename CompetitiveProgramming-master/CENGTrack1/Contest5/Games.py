n = int(input())
h1 = []
a1 = []

for _ in range(n):
    h, a = map(int,input().split())
    h1.append(h)
    a1.append(a)
    
count = 0
for i in h1:
    if i in a1:
        count += 1
    
if count == len(h1):
    print(count + 1)
    
else:
    print(count)