class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        row = len(self.matrix)
        col = len(self.matrix[0])
        self.prefix_mat = [[0]*(col+1) for _ in range(row+1)]

        for i in range(1, row+1):
            for j in range(1, col+1):
                self.prefix_mat[i][j] = self.prefix_mat[i-1][j] + self.matrix[i-1][j-1] + self.prefix_mat[i][j-1] - self.prefix_mat[i-1][j-1]
        

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_mat[row2+1][col2+1] - self.prefix_mat[row1][col2+1] - self.prefix_mat[row2+1][col1] + self.prefix_mat[row1][col1]

       