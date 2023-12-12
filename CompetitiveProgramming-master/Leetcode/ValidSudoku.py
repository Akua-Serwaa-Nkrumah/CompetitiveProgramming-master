class Solution:
    def isValidSudoku(self, board: [str]) -> bool:

        def checkSubgrid(unit):
            check = set()
            for element in unit:
                if element != '.' and element in check:
                    return False

                check.add(element)

            return True

        for row in board:
            if not checkSubgrid(row):
                return False

        for col in zip(*board):
            if not checkSubgrid(col):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                subGrid = [board[row][col] for row in range(i,i+3) for col in range(j,j+3)]

                if not checkSubgrid(subGrid):
                    return False

        return True