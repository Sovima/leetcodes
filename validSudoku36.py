def checkCol(board: List[List[str]], ind: int, col: bool):
    seen = []
    for i in range(9):
        cell = board[i][ind] if col else board[ind][i]
        if cell == '.':
            continue
        elif cell in seen:
            return True
        seen.append(cell)
    return False
        
def checkSqr(board: List[List[str]], r: int, c: int):
    seen = []
    for i in range(3):
        for j in range(3):
            cell = board[r + i][c + j]
            if cell == '.':
                continue
            elif cell in seen:
                return False
            seen.append(cell)
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if checkCol(board, i, False) or checkCol(board, i, True):
                return False
            
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not checkSqr(board, i, j):
                    return False
        return True
