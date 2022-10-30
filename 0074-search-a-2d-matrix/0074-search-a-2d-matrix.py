from bisect import bisect_left as lower_bound
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]);
        for i in matrix:
            val = lower_bound(i, target, 0, n);
            if (val < n):
                if (i[val] == target): return True
        return False