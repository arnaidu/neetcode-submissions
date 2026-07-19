public class Solution {
    public int OrangesRotting(int[][] grid) {
        Queue<(int x, int y)> q = new();
        HashSet<(int x, int y)> seen = new();
        
        int xlen = grid[0].Length;
        int ylen = grid.Length;
        int countFreshFruits = 0;
        for (int y = 0; y < ylen; y++) {
            for (int x = 0; x < xlen; x++) {
                if (grid[y][x] == 2) {
                    q.Enqueue((x, y));
                    seen.Add((x, y));
                }

                if (grid[y][x] == 1) {
                    countFreshFruits++;
                }
            }
        }

        int[][] directions =
        {
            new[] { 1, 0 },
            new[] { 0, 1 },
            new[] { -1, 0 },
            new[] { 0, -1 }
        };
        
        int time = 0;
        while (q.Count > 0) {
            int count = q.Count;
            while (count > 0) {
                var point = q.Dequeue();
                foreach (var direction in directions) {
                    int dx = direction[0];
                    int dy = direction[1];
                    int nx = point.x + dx;
                    int ny = point.y + dy;

                    if (0 > nx || nx >= xlen || ny < 0 || ny >= ylen || grid[ny][nx] != 1) {
                        continue;
                    }

                    // don't revisit
                    if (seen.Contains((nx, ny))) {
                        continue;
                    }
                    
                    countFreshFruits--;
                    q.Enqueue((nx, ny)); // fresh fruit which is now rotten
                    seen.Add((nx, ny));
                }

                count--;
            }
            
            if (q.Count > 0) {
                time++;
            }
        }
        
        if (countFreshFruits > 0) {
            return -1;
        }

        return time;
    }
}
