class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        if rowIndex <= 1:
            return [1]*(2**rowIndex)

        mat = [1]*(rowIndex + 1)
        prev = self.getRow(rowIndex -1)

        for i in range(1,rowIndex):
            mat[i] = prev[i-1] + prev[i]

        return mat

    
akua = Solution()
print(akua.getRow(3))
        
