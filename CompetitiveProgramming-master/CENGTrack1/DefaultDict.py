from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)
B = defaultdict(list)

for i in range(1,n+1):
    A[input()].append(i)
for j in range(1,m+1):
    B[input()].append(j)

for letter in B:
    if letter in A:
        print(*A[letter])
    else:
        print(-1)