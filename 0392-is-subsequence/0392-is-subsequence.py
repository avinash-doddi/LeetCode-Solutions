class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s); m = len(t); i = 0; j = 0;
        while j < m: 
            if i<n:
                if s[i]==t[j]: i,j = i+1,j+1;
                else: j+=1;
            else: break
        return i==n
            
        