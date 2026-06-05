class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nrows, ncols = len(board), len(board[0])
        def dfs(row, col):
            if 0 <= row < nrows and 0 <= col < ncols:
                if board[row][col] == "O":
                    board[row][col] = "#"
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = row + dr, col + dc
                        dfs(nr, nc)
            
        for row in range(nrows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][ncols - 1] == "O":
                dfs(row, ncols - 1)
        
        for col in range(1, ncols - 1):
            if board[0][col] == "O":
                dfs(0, col)
            if board[nrows - 1][col] == "O":
                dfs(nrows - 1, col)
        

        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] == "#":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"
        
        