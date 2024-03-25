from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    prefix = [0]

    cnt = 0

    for i in range(n):
        if s[i] == '+':
            prefix.append(prefix[-1] + 1)

        else:
            prefix.append(prefix[-1]-1)

    for i in range(n+1):
        for j in range(i+1,n+1):
            if prefix[i] >= prefix[j] and (prefix[i] - prefix[j])%3 == 0:
                cnt += 1

    print(cnt)
