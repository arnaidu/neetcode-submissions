class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        def dfs(row, col):
            # if wall or water return 1
            if row < 0 or row >= len(grid):
                return 1
            if col < 0 or col >= len(grid[0]):
                return 1
            if grid[row][col] == 0:
                return 1
            
            # else figure out perimeter
            perimeter = 0

            # if seen skip
            seen.add((row, col))
            for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if (nr, nc) in seen:
                    continue
                perimeter += dfs(nr, nc)
            return perimeter

        p = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in seen:
                    if grid[row][col] == 1:
                        p += dfs(row, col)

        return p
