t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())

    dx = abs(xk - xq)
    dy = abs(yk - yq)

    count = 0

    if (dx % a == 0 and dy % b == 0 and dx // a % 2 == dy // b % 2) or \
       (dx % b == 0 and dy % a == 0 and dx // b % 2 == dy // a % 2):
        count = 2

    print(count)