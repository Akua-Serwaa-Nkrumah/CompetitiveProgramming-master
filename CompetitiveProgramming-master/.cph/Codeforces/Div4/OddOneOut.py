from collections import Counter

t = int(input())

for _ in range(t):
    a = list(map(int,input().split()))
    a_count = Counter(a)

    for i in a_count:
        if a_count[i] == 1:
            print(i)