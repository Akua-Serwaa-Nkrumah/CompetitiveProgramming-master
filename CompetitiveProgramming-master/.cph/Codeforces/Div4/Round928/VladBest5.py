from collections import Counter

t = int(input())

for _ in range(t):
    s = list(input())

    A = 0
    B = 0

    for i in s:
        if i == 'A':
            A += 1
        else:
            B += 1

    if A > B:
        print('A')
    else:
        print('B')