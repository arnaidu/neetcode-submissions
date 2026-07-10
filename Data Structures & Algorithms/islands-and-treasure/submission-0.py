from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nrows, ncols = len(grid), len(grid[0])
        seen = set()

        q = deque([])
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 0:
                    q.append((row, col))

        distance = 1
        while q:
            nq = len(q)
            for _ in range(nq):
                row, col = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] > 0:
                        if (nr, nc) in seen:
                            continue
                        seen.add((nr, nc))
                        q.append((nr, nc))
                        grid[nr][nc] = distance
            distance += 1




            
