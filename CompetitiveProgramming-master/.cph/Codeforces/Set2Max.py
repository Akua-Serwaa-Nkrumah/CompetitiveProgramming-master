t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    l, r = 0, n

    # while l <= r and (a[l] == b[l] or a[r] == b[r]):
    #     if a[l] != b[l]:
    #         left 