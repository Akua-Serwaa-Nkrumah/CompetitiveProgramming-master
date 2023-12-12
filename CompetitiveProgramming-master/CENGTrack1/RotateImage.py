class Solution(object):
    def rotate(self, matrix):
        row = len(matrix)
        for i in range(row):
            for j in range(i, row):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
           matrix[i] = matrix[i][::-1]