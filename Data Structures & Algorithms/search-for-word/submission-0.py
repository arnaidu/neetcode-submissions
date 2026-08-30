class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows, ncols = len(board), len(board[0])
        seen = set()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def search(seen, word, row, col, index):
            nonlocal directions, nrows, ncols
            
            if board[row][col] != word[index]:
                return False

            seen.add((row, col))

            if index == len(word) - 1:
                return True


            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr, nc) in seen or nr < 0 or nr >= nrows or nc < 0 or nc >= ncols:
                    continue
                
                value = search(seen, word, nr, nc, index + 1)
                if value:
                    return True

            seen.remove((row, col))

        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] == word[0]:
                    if search(seen, word, row, col, 0):
                        return True
        return False

