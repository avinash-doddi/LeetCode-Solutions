from collections import defaultdict as maps
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ds = maps(int); dp = maps(int);
        for i in p: dp[i] += 1;
        n = len(s); m = len(p); i = 0; j = 0; indices = []
        while(j < n):
            if (j < m):
                ds[s[j]] += 1; j += 1;
            else:
                if (ds == dp): indices.append(i);
                if (ds[s[i]] > 1): ds[s[i]] -= 1;
                else: del ds[s[i]];
                ds[s[j]] += 1; i += 1; j += 1;
        if (ds == dp): indices.append(i)
        return indices
        
            