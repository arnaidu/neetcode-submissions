public class Solution {
    private (int dc, int dr)[] directions = {
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 0)
    };

    public int NumIslands(char[][] grid) {
        int nrows = grid.Length;
        int ncols = grid[0].Length;
        int numIslands = 0;
        for (int row = 0; row < nrows; row++) {
            for (int col = 0; col < ncols; col++) {
                char val = grid[row][col];
                if (val == '1') {
                    Search(grid, row, col, nrows, ncols);
                    numIslands++;
                }
            }
        }

        return numIslands;
    }

    public void Search(char[][] grid, int startRow, int startCol, int nrows, int ncols) {
        grid[startRow][startCol] = '0';
        foreach(var direction in directions) {
            int nc = startCol + direction.dc;
            int nr = startRow + direction.dr;
            if (nr < 0 || nr >= nrows || nc < 0 || nc >= ncols || grid[nr][nc] == '0') {
                continue;
            }

            Search(grid, nr, nc, nrows, ncols);
        }
    }
}
