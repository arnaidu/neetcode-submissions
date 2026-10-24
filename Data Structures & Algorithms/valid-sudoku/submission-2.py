from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = defaultdict(set)
        seen_col = defaultdict(set)
        seen_3_by_3 = defaultdict(set)

        nrows, ncols = len(board), len(board[0])
        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] == ".":
                    continue
                if (
                    self.seen_in_row(row, col, seen_row, board) or 
                    self.seen_in_col(row, col, seen_col, board) or
                    self.seen_in_3_by_3(row, col, seen_3_by_3, board)):
                    return False
        return True


    def seen_in_row(self, row, col, seen_row, board) -> bool:
        cell_value = board[row][col]
        if cell_value not in seen_row[row]:
            seen_row[row].add(cell_value)
            return False
        return True
    
    def seen_in_col(self, row, col, seen_col, board) -> bool:
        cell_value = board[row][col]
        if cell_value not in seen_col[col]:
            seen_col[col].add(cell_value)
            return False
        return True
    
    def seen_in_3_by_3(self, row, col, seen_3_by_3, board) -> bool:
        cell_value = board[row][col]
        top_left = (row // 3, col // 3)
        if cell_value not in seen_3_by_3[top_left]:
            seen_3_by_3[top_left].add(cell_value)
            return False
        return True
