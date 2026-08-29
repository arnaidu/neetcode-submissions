class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        ncols = len(matrix[0])
        lower, upper = 0, nrows * ncols - 1
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            row = mid // ncols
            col = mid % ncols
            midpoint = matrix[row][col]
            if target == midpoint:
                return True
            elif target > midpoint:
                lower = mid + 1
            else:
                upper = mid - 1
        return False