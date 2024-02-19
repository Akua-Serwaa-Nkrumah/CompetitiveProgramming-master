t = int(input())
for _ in range(t):
    n = int(input())

    grid = []
    for _ in range(n):
        i = input()
        i.zfill(n)
        i = list(i)
        grid.append(i)

    lis = []

    for i in range(n):
        cnt = 0
        for j in range(n):
            if grid[i][j] == '1':
                cnt += 1

        lis.append(cnt)

    lis.sort()

    for i in range(len(lis)-1):
        if lis[i] != 0:
            if lis[i] == lis[i+1]:
                print('SQUARE')
                break
            else:
                print("TRIANGLE")
                break