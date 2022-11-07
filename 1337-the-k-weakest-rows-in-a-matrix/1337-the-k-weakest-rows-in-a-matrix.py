class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}; n = len(mat); arr = []
        for i in range(n):
            x = mat[i].count(1);
            d[i] = x; arr.append(i);
        arr.sort(key = lambda i: d[i]);
        return arr[:k]
        