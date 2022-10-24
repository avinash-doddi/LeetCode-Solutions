class Solution:
    
    def bfs(self, grid, i, j, n, m):
        if (i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0): return
        if (grid[i][j]):
            self.count += 1; grid[i][j] = 0;
        self.bfs(grid, i-1, j, n, m);
        self.bfs(grid, i+1, j, n, m);
        self.bfs(grid, i, j-1, n, m);
        self.bfs(grid, i, j+1, n, m);
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid); m = len(grid[0]); self.count = 0; maxval = 0;
        for i in range(n):
            for j in range(m):
                if (grid[i][j]):
                    self.bfs(grid, i, j, n, m);
                    maxval = max(maxval, self.count); self.count = 0;
        return maxval