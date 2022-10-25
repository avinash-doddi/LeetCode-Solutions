from collections import defaultdict as maps
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ds1 = maps(int); ds2 = maps(int);
        for i in s1: ds1[i] += 1;
        m = len(s1); n = len(s2);
        i = 0; j = 0;
        while(j < n):
            if (j < m):
                ds2[s2[j]] += 1; j += 1;
            else:
                if (ds1 == ds2): return True
                if (ds2[s2[i]] > 1): ds2[s2[i]]-=1;
                else: del ds2[s2[i]];
                ds2[s2[j]] += 1; i += 1; j += 1
        if (ds1 == ds2): return True
        return False
            
            