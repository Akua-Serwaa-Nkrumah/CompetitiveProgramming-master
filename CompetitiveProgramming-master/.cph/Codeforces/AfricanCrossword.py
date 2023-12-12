rows, cols = map(int,input().split())
col = list(map(list,input().split()))
grid = [col for _ in range(rows)]

print(zip(*grid))
