t = int(input())

for _ in range(t):
    s = input()
    s = 'R' + s +'R'

    l, r = 0, 1

    arr = []

    while l < r and r < len(s):
        if s[r] == 'R' and s[l] == 'R':
            arr.append(r-l)
            l = r

        r += 1

    print(max(arr))
# Farad
# for _ in range(int(input())):
#     a = list(map(len,input().split('R')))
#     print(max(a)+1)


        