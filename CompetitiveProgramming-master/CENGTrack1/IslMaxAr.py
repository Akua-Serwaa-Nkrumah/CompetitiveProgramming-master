class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        visited = set()
        num = 0
        mx = 0

        def dfs(i,j):
            nonlocal num, mx
            if not (-1<i<len(grid)) or not(-1<j<len(grid[0])):
                return 0

            if grid[i][j] == 0:
                return 0
   
            if (i,j) in visited:
                return 0

            visited.add((i,j))

            num =  (1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1))

            return num
          

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    mx = max(mx,dfs(i,j))

        return mx
    