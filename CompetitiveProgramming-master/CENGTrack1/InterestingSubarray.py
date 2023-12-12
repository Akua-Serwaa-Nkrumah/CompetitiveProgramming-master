n = int(input())
for _ in range(n):
    length = int(input())
    values = sorted(list(map(int,input().split())))
    if max(values)-min(values) >= length:
        print("YES")
        values.remove(max(values))
        values.remove(min(values))
        if max(values)-min(values) >= len(values):
            print(*values)
        else:
            values[-1] = 2*max(values)-min(values)
            print(*values)
    else:
        print("NO")