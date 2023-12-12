class Solution(object):
    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        rows_to_zero = set()
        cols_to_zero = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        for i in range(row):
            for j in range(col):
                if i in rows_to_zero or j in cols_to_zero:
                    matrix[i][j] = 0