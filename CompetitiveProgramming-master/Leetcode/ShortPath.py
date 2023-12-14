from queue import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        row, col = len(grid), len(grid[0])
        mn = 1
        visited = set()
    
        queue = deque([(0,0)])
        directions = [(-1,-1),(-1,0),(-1, 1), (0, 1), (1, 0), (1, 1), (1,-1), (0,-1)]

        while queue:
            length = len(queue)

            for _ in range(length):
                i, j = queue.popleft()

                if grid[i][j] == 1 or (i, j) in visited:
                    continue
                
                if (i, j) == (row-1,col-1):
                    return mn
                
                visited.add((i, j))

                for (dx, dy) in directions:
                    if (-1 < i+dx < row) and (-1<j+dy<col):
                        queue.append((i+dx,j+dy))

            mn += 1
        return -1