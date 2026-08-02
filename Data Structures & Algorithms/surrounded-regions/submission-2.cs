public class Solution {
    private List<(int dr, int dc)> _directions = [
        (1, 0),
        (0, 1),
        (0, -1),
        (-1, 0)
    ];

    public void Solve(char[][] board) {
        int nrows = board.Length;
        int ncols = board[0].Length;
        for (int row = 0; row < nrows; row++) {
            DFS(board, row, 0, nrows, ncols);
            DFS(board, row, ncols - 1, nrows, ncols);
        }

        for (int col = 0; col < ncols; col++) {
            DFS(board, 0, col, nrows, ncols);
            DFS(board, nrows - 1, col, nrows, ncols);
        }

        // if we haven't seen it, then set to 'X'
        for (int row = 0; row < nrows; row++) {
            for (int col = 0; col < ncols; col++) {
                if (board[row][col] == 'T')
                    board[row][col] = 'O';
                else if (board[row][col] == 'O')
                    board[row][col] = 'X';
            }
        }
    }

    public void DFS(char[][] board, int row, int col, int nrows, int ncols) {
        if (board[row][col] != 'O') {
            return;
        }

        board[row][col] = 'T';

        foreach (var direction in _directions) {
            var (nr, nc) = (direction.dr + row, direction.dc + col);
            if (nr < 0 || nr >= nrows || nc < 0 || nc >= ncols || board[nr][nc] != 'O') {
                continue;
            }

            DFS(board, nr, nc, nrows, ncols);
        }
    }
}
