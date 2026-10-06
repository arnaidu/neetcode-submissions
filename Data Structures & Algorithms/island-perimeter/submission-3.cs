public class Solution {
    private (int, int)[] _directions = [
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1)
    ];

    private int _perimeter = 0;

    public int IslandPerimeter(int[][] grid) {
        for (int row = 0; row < grid.Length; row++) {
            for (int col = 0; col < grid[0].Length; col++) {
                if (grid[row][col] == 1) {
                    dfs(grid, row, col);
                    return _perimeter;
                }
            }
        }

        return _perimeter;
    }

    public void dfs(int[][] grid, int row, int col) {
        grid[row][col] = -1; // mark as visited
        foreach (var (dr, dc) in _directions) {
            var (nr, nc) = (row + dr, col + dc);
            // we are hitting top or bottom wall
            if (nr < 0 || nr >= grid.Length) {
                _perimeter += 1;
                continue;
            }

            // we are hitting right or left wall
            if (nc < 0 || nc >= grid[0].Length) {
                _perimeter += 1;
                continue;
            }
            
            // we are hitting water
            if (grid[nr][nc] == 0) {
                _perimeter += 1;
                continue;
            }

            // we are at another land block
            if (grid[nr][nc] == 1) {
                dfs(grid, nr, nc);
            }
        }
    }
}