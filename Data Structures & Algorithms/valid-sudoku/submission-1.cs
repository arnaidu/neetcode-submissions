public class Solution {
    public bool IsValidSudoku(char[][] board) {
        int nrows = board.Length;
        int ncols = board[0].Length;
        Dictionary<int, HashSet<char>> seenInRow = new();
        Dictionary<int, HashSet<char>> seenInCol = new();
        Dictionary<(int, int), HashSet<char>> seenInSquare = new();
        for (int row = 0; row < nrows; row++) {
            for (int col = 0; col < ncols; col++) {
                char val = board[row][col];
                if (val == '.') {
                    continue;
                }
                if (!SeenInRow(val, seenInRow, row)){
                    return false;
                }
                if (!SeenInCol(val, seenInCol, col)) {
                    return false;
                }
                if (!SeenInSquare(val, seenInSquare, row, col)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    public bool SeenInSquare(char value, Dictionary<(int, int), HashSet<char>> seenInSquare, int row, int col) {
        var squareId = (row / 3, col / 3);
        if (!seenInSquare.TryGetValue(squareId, out var seen)) {
            seen = new();
            seenInSquare[squareId] = seen;
        }
        
        return seen.Add(value);
    }
    
    public bool SeenInRow(char value, Dictionary<int, HashSet<char>> seenInRow, int row) {
        if (!seenInRow.TryGetValue(row, out var seen))
        {
            seen = new();
            seenInRow[row] = seen;
        }

        return seen.Add(value);
    }
    
    public bool SeenInCol(char value, Dictionary<int, HashSet<char>> seenInCol, int col) {
        
        if (!seenInCol.TryGetValue(col, out var seen))
        {
            seen = new();
            seenInCol[col] = seen;
        }
        
        return seen.Add(value);
    }
}