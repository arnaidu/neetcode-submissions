class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        max_area = 0
        def dfs(row, col):
            if 0 <= row < nrows and 0 <= col < ncols:
                if grid[row][col] == 0:
                    return 0
                
                grid[row][col] = 0
                return 1 + (
                    dfs(row + 1, col) +
                    dfs(row, col + 1) +
                    dfs(row, col - 1) +
                    dfs(row - 1, col)
                )
            return 0
        
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(max_area, area)
        return max_area

