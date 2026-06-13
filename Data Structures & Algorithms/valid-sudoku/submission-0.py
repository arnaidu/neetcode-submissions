class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        sub_boxes = {}
        valid_numbers = { '1', '2', '3', '4', '5', '6', '7', '8', '9' }
        def get_subbox(row, col):
            subbox_row = row // 3 # if row = 3, then idx subbox is 1 
            subbox_col = col // 3 # if col = 5, then idx subbox is 2
            return subbox_row, subbox_col
        
        def handle_subbox(row, col, number_string, sub_boxes):
            subbox = get_subbox(row, col)
            if subbox not in sub_boxes:
                sub_boxes[subbox] = set()
            else:
                if number_string in sub_boxes[subbox]:
                    return False

            sub_boxes[subbox].add(number_string)
            return True

        def handle_row_col(row, col, rows, cols, number_string):
            if row not in rows:
                rows[row] = set()
            
            if col not in cols:
                cols[col] = set()
            
            if number_string in rows[row]:
                return False
            
            if number_string in cols[col]:
                return False
            
            rows[row].add(number_string)
            cols[col].add(number_string)
            return True

        for row in range(len(board)):
            for col in range(len(board[0])):
                number_string = board[row][col]
                if number_string not in valid_numbers:
                    continue
                isGood = handle_subbox(row, col, number_string, sub_boxes)
                isGood1 = handle_row_col(row, col, rows, cols, number_string)
                if not isGood or not isGood1:
                    return False

        return True



