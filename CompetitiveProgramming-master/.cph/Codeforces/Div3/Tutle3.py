from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int,input().split()))

    a_count = Counter(a)

    total = sum(a)

    if total%3 == 0:
        print(0)

    else:
        add = 3 - total%3
        sub = total%3

        for i in a_count:
            if i != 1 and i%sub == 0:
                print(1)
