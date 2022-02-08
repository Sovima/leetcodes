class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = -1
        c = len(matrix[0])
        end = len(matrix)
        arr = None
        while 1:
            if start == end - 1:
                return False
            middle = (start + end) // 2
            arr = matrix[middle]
            if (target < arr[0]):
                end = middle
            elif (target > arr[c - 1]):
                start = middle
            else:
                start = -1
                end = c
                while 1:
                    if start == end - 1:
                        return False
                    middle = (start + end) // 2
                    cell = arr[middle]
                    if (target < cell):
                        end = middle
                    elif (target > cell):
                        start = middle
                    else:
                        return True    
