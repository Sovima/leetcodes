class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        l = 1
        for i in range(1, numRows):
            l += 1
            row = [1] 
            row += [out[i-1][j] + out[i-1][j+1] for j in range(0, l - 2)]
            row += [1]
            out.append(row)
        return out
        
