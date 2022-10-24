class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix); temp = []
        for i in range(n):
            ref = [];
            for j in range(n):
                ref.append(matrix[j][i])
            ref.reverse(); temp.append(ref); del ref;
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[i][j];