from numpy import *
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = matrix(mat); ans = 0; n = len(mat)
        ans += sum(m.diagonal()); m = fliplr(m);
        ans += sum(m.diagonal()); 
        if (n & 1): ans -= mat[n//2][n//2];
        return ans
        