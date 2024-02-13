t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    f = input()
    cat_added = 0
    cat_removed = 0

    for i in range(n):
        if s[i] == '0' and f[i] == '1':
            cat_added += 1
        elif s[i] == '1' and f[i] == '0':
            cat_removed += 1

    print(max(cat_added, cat_removed))


