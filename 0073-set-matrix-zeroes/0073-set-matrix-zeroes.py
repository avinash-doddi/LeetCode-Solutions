class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []; n = len(matrix); m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if (matrix[i][j] == 0):
                    zeros.append([i,j]);
        for x, y in zeros:
            for i in range(m):
                matrix[x][i] = 0;
            for i in range(n):
                matrix[i][y] = 0;
                