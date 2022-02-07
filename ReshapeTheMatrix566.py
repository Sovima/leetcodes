class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if m * n != r * c:
            return mat
        out = [ [ None for i in range(c) ] for j in range(r) ]
        currR = 0
        currC = 0
        for i in range(n):
            for j in range(m):
                out[currR][currC] = mat[i][j]
                currC += 1
                if currC > c - 1:
                    currR += 1
                    currC = 0
        return out 
