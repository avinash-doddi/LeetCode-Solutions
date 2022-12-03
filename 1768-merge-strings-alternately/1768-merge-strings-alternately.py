class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        i = 0; j = 0; n = len(w1); m = len(w2); fin = ''
        while True:
            if (i == n and j == m): return fin
            if (i < n):
                fin += w1[i]; i += 1;
            if j < m:
                fin += w2[j]; j += 1;
        
            
            
        