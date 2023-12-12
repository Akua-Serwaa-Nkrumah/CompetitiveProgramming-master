class Solution(object):
    def numMagicSquaresInside(self, grid):
        
        def is_magic_square(grid, row, col):
            target_sum = sum(grid[row][col:col+3]) 
            
            for i in range(3): #rows
                if sum(grid[row+i][col:col+3]) != target_sum:
                    return False
            for j in range(3): #colums
                if sum(grid[row+i][col+j] for i in range(3)) != target_sum:
                    return False
            if sum(grid[row+i][col+i] for i in range(3)) != target_sum:#primary_diag
                return False
            if sum(grid[row+i][col+2-i] for i in range(3)) != target_sum:#second_diag
                return False
            return True

        
        def distinct(grid,row,col):
            distinct_grid = set()
            for a in range(3):
                for b in range(3):
                    if 1 <= grid[row+a][col+b] <= 9:
                        distinct_grid.add(grid[row+a][col+b])

            if len(distinct_grid) == 9:
                return True
            return False

        rows = len(grid)
        cols = len(grid[0])
        max_square = 0
        
        
        for i in range(rows-2):
            for j in range(cols-2):
                if distinct(grid,i,j):
                    if is_magic_square(grid, i, j):
                        max_square += 1
        return max_square
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        