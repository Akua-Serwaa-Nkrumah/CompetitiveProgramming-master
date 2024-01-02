t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    stack = []
    for i in a:
        if stack:
            if (stack[-1] < 0 and i < 0) or (stack[-1] > 0 and i > 0):
                if stack[-1] < i:
                    stack[-1] = i

            else:
                 stack.append(i)

        else:
            stack.append(i)

    print(sum(stack))