public class Solution {
    public int IslandPerimeter(int[][] grid) {
        var (nrows, ncols) = (grid.Length, grid[0].Length);
        bool[,] visited = new bool[nrows, ncols];
        for (int i = 0; i < nrows; i++) {
            for (int j = 0; j < ncols; j++) {
                if (grid[i][j] == 1) {
                    return dfs(i, j, grid, visited);
                }
            }
        }
        return 0;
    }

    public int dfs(int row, int col, int[][] grid, bool[,] visited) {
        if (visited[row, col]) {
            // skip if visited
            return 0;
        }

        visited[row, col] = true;
        var perimeter = 0;
        var (nrows, ncols) = (grid.Length, grid[0].Length);
        (int dr, int dc)[] directions =
        {
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        };

        foreach (var (dr, dc) in directions) {
            var (nr, nc) = (row + dr, col + dc);

            if (nr < 0 || nr >= nrows || nc < 0 || nc >= ncols) {
                // we hit a wall so incrmeent perimeter
                perimeter++;
            }
            else if (grid[nr][nc] == 0) {
                // we hit water
                perimeter++;
            }
            else {
                perimeter += dfs(nr, nc, grid, visited);
            }
        }

        return perimeter;
    }
}