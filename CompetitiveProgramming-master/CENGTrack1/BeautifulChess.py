t = int(input())

for i in range(t):
    input()
    chess = []
    for _ in range(1,9):
        chess.append(input())

    rows = len(chess)
    cols = len(chess[0])
    for row in range(1,rows-1):
        for col in range(1,cols-1):
            if chess[row][col] == "#":
                if chess[row-1][col-1] == "#" and chess[row+1][col+1] == "#" and chess[row - 1][col+1] == "#" and chess[row+1][col-1] == "#":
                    print(row+1,col+1)