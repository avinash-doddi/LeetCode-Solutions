class Solution:
    def recur(self, mat, i, j, n, m, ref):
        if (i < 0 or j < 0 or i >= n or j >= m): return
        ref.append(mat[i][j])
        self.recur(mat, i+1, j-1, n, m, ref); 
        
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat); m = len(mat[0]);
        if (n == 1 and m == 1): return mat[0];
        newarr = []
        for i in range(1):
            for j in range(m):
                ref = [];
                self.recur(mat, i, j, n, m, ref);
                newarr.append(ref);
        i = 1; j = m-1;
        while(i < n):
            ref = [];
            self.recur(mat, i, j, n, m, ref);
            newarr.append(ref); i += 1;
        returnarr = []
        n = len(newarr);
        for i in range(n):
            if (i&1):
                for j in newarr[i]:
                    returnarr.append(j);
            else:
                for j in reversed(newarr[i]):
                    returnarr.append(j);
        return returnarr
        
                