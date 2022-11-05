class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        newarr = []; n = len(matrix)
        for i in matrix:
            for j in i: newarr.append(j);
        newarr.sort();
        return newarr[k-1]