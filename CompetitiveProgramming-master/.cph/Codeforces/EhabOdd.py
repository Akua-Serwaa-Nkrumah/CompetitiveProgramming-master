n = int(input())
a = list(map(int,input().split()))
odd, even = 0, 0

for num in a:
    if num%2 == 1:
        odd += 1
    else: 
        even += 1

if odd != 0 and even != 0:
    a.sort()

print(*a)