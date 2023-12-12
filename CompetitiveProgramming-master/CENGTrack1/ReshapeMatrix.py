class Solution(object):
    def matrixReshape(self, mat, r, c):
        row = len(mat)
        col = len(mat[0])
        new_mat=[[0]*c for i in range(r)]
        if (row)*(col)==(r*c):
            for i in range(row):
                for j in range(col):
                    linear_index = i * col + j
                    new_row = linear_index // c
                    new_col = linear_index % c
                    new_mat[new_row][new_col] = mat[i][j]
            return new_mat
        else:
            return mat