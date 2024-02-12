t = int(input())

for _ in range(t):
    s = input()
    c = input()
    pos = []
    check = False

    for i in range(len(s)):
        if s[i] == c:
            if not ((i+1)%2 == 0 and (len(s)-(i-1))%2 == 1):
                if not check:
                    check = True

    if check:
        print("YES")
    else:
        print("NO")