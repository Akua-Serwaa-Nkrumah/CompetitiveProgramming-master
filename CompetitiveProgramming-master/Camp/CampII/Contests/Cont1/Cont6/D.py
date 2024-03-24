from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if '+' not in s or '-' not in s:
        print(s.count('-')//2)
    else:
        cnt = 0
        minus, plus = 0, 0
        stack = deque([])
        for i in range(n):
            if stack:
                if (s[i] == '+' and stack[-1] == '-') or (s[i] == '-'):
                    cnt += 1
                
                stack.popleft()
            stack.append(s[i])

        if s.count('+') == s.count('-'):
            cnt += 1

        print(cnt)
