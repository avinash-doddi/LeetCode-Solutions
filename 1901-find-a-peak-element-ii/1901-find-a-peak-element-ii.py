class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def check(mat, i, j, r, c):
            if (i-1 >= 0 and i-1 < r):
                if (mat[i][j] < mat[i-1][j]): return False
            if (i+1 >= 0 and i+1 < r):
                if (mat[i][j] < mat[i+1][j]): return False
            if (j-1 >= 0 and j-1 < c):
                if (mat[i][j] < mat[i][j-1]): return False
            if (j+1 >= 0 and j+1 < c):
                if (mat[i][j] < mat[i][j+1]): return False
            return True
                
        r = len(mat); c = len(mat[0]);
        for i in range(r):
            for j in range(c):
                if (check(mat, i, j, r, c)):
                    return [i, j]