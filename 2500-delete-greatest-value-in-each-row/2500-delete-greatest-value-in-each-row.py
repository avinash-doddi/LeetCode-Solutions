class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort(reverse = True)
        finalsum = 0
        for i in range(len(grid[0])):
            maxx = 0;
            for j in range(len(grid)):
                maxx = max(maxx, grid[j][i])
            finalsum += maxx
        return finalsum
            