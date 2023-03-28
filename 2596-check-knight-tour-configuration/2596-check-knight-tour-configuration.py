class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid); m = len(grid[0]);
        dp = [(-2,-1),(+2,-1),(-2,+1), (+2, +1), (-1,-2), (+1, -2), (-1,+2), (+1,+2)]
        d = {grid[i][j]:(i,j) for i in range(n) for j in range(m)}
        total = (n*m) - 1; i = 0;
        if d[0] != (0,0): return False
        while i < total:
            row, col = d[i]; found = 0;
            for a,b in dp:
                r = row + a; c = col + b;
                if r < n and r >= 0 and c < m and c >= 0:
                    if grid[r][c] == i+1:
                        found = 1; break;
            if not found: 
                return False
            i += 1;
        return True