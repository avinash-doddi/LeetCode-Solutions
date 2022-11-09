class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def traverse(grid, i, j, n, m):
            summ = 0
            summ += (grid[i][j] + grid[i][j+1] + grid[i][j+2]);              #######
            summ += grid[i+1][j+1];                                             #
            summ += (grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]);        #######
            return summ;
            
            
        n = len(grid); m = len(grid[0]); maxsum = 0;
        for i in range(n-2):
            for j in range(m-2):
                maxsum = max(maxsum, traverse(grid, i, j, n, m));
        return maxsum