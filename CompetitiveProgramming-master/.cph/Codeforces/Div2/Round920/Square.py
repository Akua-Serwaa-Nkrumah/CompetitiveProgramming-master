t = int(input())
for _ in range(t):
    x_corners = set()
    y_corners = set()
    for i in range(4):
        x, y = map(int,input().split())
        x_corners.add(x)
        y_corners.add(y)

    x_corners = sorted(x_corners)
    y_corners = sorted(y_corners)

    print((x_corners[1] - x_corners[0])*(y_corners[1] - y_corners[0]))
    