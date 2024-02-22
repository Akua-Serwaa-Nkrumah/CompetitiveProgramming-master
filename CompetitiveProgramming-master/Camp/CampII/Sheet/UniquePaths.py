# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         memo = {}

#         def dp(i,j):
#             if i >= m or j >= n:
#                 return 0

#             if (i,j) == (m-1,n-1):
#                 return 1

#             if (i,j) not in memo:
#                 memo[(i,j)] = dp(i+1,j) + dp(i,j+1)

#             return memo[(i,j)]

#         return dp(0,0)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n+1)] for _ in range(m+1)]

        grid[m-1][n-1] = 1
    
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                grid[i][j] += grid[i+1][j] + grid[i][j+1]

        print(grid)

        return grid[0][0]