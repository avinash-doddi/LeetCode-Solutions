from collections import defaultdict as maps
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = maps(int)
        for i in grid:
            d[tuple(i)] += 1;
        n = len(grid); count = 0
        for i in range(n):
            arr = []
            for j in range(n):
                arr.append(grid[j][i]);
            arr = tuple(arr)
            if (d[arr]):
                count = count + d[arr];
        return count
                
                
                