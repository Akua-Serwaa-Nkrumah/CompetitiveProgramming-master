class Solution(object):
    def diagonalSum(self, mat):
        prim_diag = []
        n = len(mat)
        for i in range(len(mat)):
            prim_diag.append(mat[i][i])
        secon_diag = []
        for j in range(len(mat)):
            secon_diag.append(mat[j][n-1-j])
        if len(mat)%2 == 1:
            for k in range(len(mat)):
                if(mat[k] == mat[n-1-k]):
                    overlap = mat[k][n-1-k]
            total = secon_diag + prim_diag
            total.remove(overlap)
        else:
            total = secon_diag + prim_diag
        summer = sum(total)
        return summer
        
        
akua = Solution()
print(akua.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))