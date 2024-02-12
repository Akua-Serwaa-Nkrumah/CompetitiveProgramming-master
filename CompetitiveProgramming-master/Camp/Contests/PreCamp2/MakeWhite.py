t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    l, r = 0, n -1

    while l < n and s[l] == 'W':
        l += 1

    while r > -1 and s[r] == 'W':
        r -= 1

    print(r-l+1) if r-l+1 > 0 else print(0)