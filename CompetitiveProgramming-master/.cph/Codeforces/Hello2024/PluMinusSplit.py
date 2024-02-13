t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    pos, neg = 0, 0

    for i in s:
        if i == '+':
            pos += 1
        else:
            neg += 1

    print(abs(pos-neg))