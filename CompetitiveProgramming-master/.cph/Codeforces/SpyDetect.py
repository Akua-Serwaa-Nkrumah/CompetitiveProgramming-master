from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    a_count = Counter()

    for i in a_count:
        if a_count[i] == 1:
            print(i)
