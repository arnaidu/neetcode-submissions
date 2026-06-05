from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        q = deque([])
        seen = set()
        nrows, ncols = len(grid), len(grid[0])
        def dfs(row, col):
            if (row, col) in seen:
                return
            if 0 <= row < nrows and 0 <= col < ncols:
                if grid[row][col] == 0:
                    return
                seen.add((row, col))
                q.append((row, col, 0))
                seen.add((row, col))
                for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    dfs(row + dr, col + dc)


        for row in range(nrows):
            seenIsland = False
            for col in range(ncols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    seenIsland = True
                    break
            if seenIsland:
                break

        while q:
            nqueue = len(q)
            for _ in range(nqueue):
                row, col, distance = q.popleft()
                for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    nr, nc = row + dr, col + dc
                    if (nr, nc) in seen:
                        continue
                    if 0 <= nr < nrows and 0 <= nc < ncols:
                        if grid[nr][nc] == 0:
                            seen.add((nr, nc))
                            q.append((nr, nc, distance + 1))
                        else:
                            return distance           



        