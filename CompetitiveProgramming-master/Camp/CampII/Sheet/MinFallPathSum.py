class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        dp = [[10000 for _ in range(len(matrix)+2)] for _ in range(len(matrix)+1)]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                dp[i][j+1] = matrix[i][j]

        for i in range(len(matrix)-2,-1,-1):
            for j in range(len(matrix),0,-1):
                dp[i][j] += min(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])
        
        return min(dp[0])