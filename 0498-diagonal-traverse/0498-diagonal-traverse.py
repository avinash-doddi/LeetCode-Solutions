class Solution:
    def recursion(self, mat, i, j, n, m, ref):
        if (i < 0 or j < 0 or i >= n or j >= m): return
        ref.append(mat[i][j])
        self.recursion(mat, i+1, j-1, n, m, ref); 
    
    #this is to get diagonal elements in reverse 
    def reverse_recursion(self, mat, i, j, n, m, ref):
        if (i < 0 or j < 0 or i >= n or j >= m): return
        self.reverse_recursion(mat, i+1, j-1, n, m, ref); 
        ref.append(mat[i][j])
        
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat); m = len(mat[0]);
        if (n == 1 and m == 1): return mat[0];
        newarr = []; temp = 1; #temporary variable
        for i in range(1):
            for j in range(m):
                ref = [];
                """here we are taking a temporary variable to       differenciate which elements we want to reverse""" 
                if (temp & 1):
                    self.reverse_recursion(mat, i, j, n, m, ref);
                else:
                    self.recursion(mat, i, j, n, m, ref);
                newarr.append(ref);
                temp += 1;
        i = 1; j = m-1;
        while(i < n):
            ref = [];
            if (temp & 1):
                self.reverse_recursion(mat, i, j, n, m, ref);
            else:
                self.recursion(mat, i, j, n, m, ref);
            newarr.append(ref); i += 1; temp += 1;
        returnarr = [] # list to store final elements
        for i in newarr:
            for ele in i: 
                returnarr.append(ele)
        return returnarr
        
                