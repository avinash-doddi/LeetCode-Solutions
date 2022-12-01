class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def retrieve(mat, i, j, n, m, arr):
            if (i >= n or j >= m): return
            arr.append(mat[i][j])
            retrieve(mat, i+1, j+1, n, m, arr);
        def insert(mat, i, j, n, m, arr, k):
            if (i >= n or j >= m): return
            mat[i][j] = arr[k];
            insert(mat, i+1, j+1, n, m, arr, k+1);
        n = len(mat); m = len(mat[0]); arr = []
        '''I am traversing in this way
            ####### ->
            #
            #
            #
        '''
        for i in range(n-1, 0, -1): #""" 1st column traverse but from down to up """
            retrieve(mat, i, 0, n, m, arr);
            arr.sort();
            insert(mat, i, 0, n, m, arr, 0); arr = [];
        for i in range(0, m):  #""" 1st row traverse left to right """
            retrieve(mat, 0, i, n, m, arr);
            arr.sort();
            insert(mat, 0, i, n, m, arr, 0); arr = [];
        return mat
        
            