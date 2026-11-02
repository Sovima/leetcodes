class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) < 1:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        if cols < 1:
            return
        zero_row = False
        zero_col = False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_row = True
                    if j == 0:
                        zero_col = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        for i in range(1, rows):
            if matrix[i][0] == 0:
                matrix[i] = [0] * cols
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        if zero_row:
            matrix[0] = [0] * cols
        if zero_col:
            for i in range(0, rows):
                    matrix[i][0] = 0
      
            
        
        return matrix
        
                
        
        
        
