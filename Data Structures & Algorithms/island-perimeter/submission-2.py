class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        def dfs(row, col, grid, nrows, ncols):
            perimeter = 0
            if grid[row][col] == -1:
                return perimeter
            grid[row][col] = -1
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 > nr or nr >= nrows:
                    perimeter += 1
                elif 0 > nc or nc >= ncols:
                    perimeter += 1
                elif grid[nr][nc] == 0:
                    perimeter += 1
                else:
                    perimeter += dfs(nr, nc, grid, nrows, ncols)
                
            return perimeter
                

                
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 1:
                    return dfs(row, col, grid, nrows, ncols)
        return 0
    
