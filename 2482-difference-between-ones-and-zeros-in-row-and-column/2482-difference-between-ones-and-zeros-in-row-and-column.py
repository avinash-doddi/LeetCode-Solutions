from collections import defaultdict as maps
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row = []; col = []
        n = len(grid); m = len(grid[0])
        for i in range(n):
            one = grid[i].count(1)
            zero = grid[i].count(0);
            row.append([zero, one]);
        for i in range(m):
            one = 0; zero = 0
            for j in range(n):
                if (grid[j][i] == 1): one += 1;
                if (grid[j][i] == 0): zero += 1;
            col.append([zero, one]);
        fin = []
        for i in range(n):
            ref = [];
            for j in range(m):
                ans = row[i][1] + col[j][1] - row[i][0] - col[j][0];
                #print(i, j, ans)
                ref.append(ans);
            fin.append(ref);
        #print(fin)
        return fin
        
                