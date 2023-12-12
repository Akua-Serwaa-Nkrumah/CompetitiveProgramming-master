class Solution:
    def numIslands(self, grid: str) -> int:
        visited = set()
        num = 0

        def dfs(i, j, visited):
            if not (-1<i<len(grid)) or not ( -1 <j < len(grid[0])):
                return
            
            if (i,j) in visited or grid[i][j] == "0":
                return
            
            visited.add((i,j))

            dfs(i,j-1,visited)
            dfs(i,j+1,visited)
            dfs(i-1,j,visited)
            dfs(i+1,j,visited)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    num += 1
                    dfs(i, j, visited)

        return num
        