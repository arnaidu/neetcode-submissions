class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nrows, ncols = len(heights), len(heights[0])
        
        # collect pacific and atlantic
        pacific_seen = set()
        pacific = []

        atlantic_seen = set()
        atlantic = []
        for i in range(ncols):
            pacific.append((0, i))
            atlantic.append((nrows - 1, i))
        
        for i in range(nrows):
            pacific.append((i, 0))
            atlantic.append((i, ncols - 1))
        
        while pacific:
            cell = pacific.pop()
            row, col = cell

            pacific_seen.add(cell)
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if (nr, nc) in pacific_seen:
                    continue

                if 0 <= nr < nrows and 0 <= nc < ncols and heights[nr][nc] >= heights[row][col]:
                    pacific.append((nr, nc))

        
        while atlantic:
            cell = atlantic.pop()
            row, col = cell

            atlantic_seen.add(cell)

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc

                if (nr, nc) in atlantic_seen:
                    continue

                if 0 <= nr < nrows and 0 <= nc < ncols and heights[nr][nc] >= heights[row][col]:
                    atlantic.append((nr, nc))

        return list(pacific_seen.intersection(atlantic_seen))
