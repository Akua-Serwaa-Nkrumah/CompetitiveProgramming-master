t = int(input())

for _ in range(t):
    n = int(input())

    s = input()

    stack = ""
    cnt = 0
    for i in s:
        stack += i
        if len(stack) >= 3:
            check = stack[-3:]
            if check == 'pie' or check == 'map':
                cnt += 1
                stack = stack[:-3]

    print(cnt)