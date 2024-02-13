t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    mx = 0

    for i in s:
        mx = max(mx, ord(i) - 96)

    print(mx)