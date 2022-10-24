from collections import defaultdict as maps
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ds1 = maps(int); ds2 = maps(int)
        for i in s1: ds1[i] += 1;
        for i in s2: ds2[i] += 1;
        if (ds1 == ds2): return True;
        del ds2; ds2 = maps(int); i = 0; j = 0; n = len(s2); m = len(s1);
        while(j < n):
            if (j < m):
                ds2[s2[j]] += 1; j += 1;
            elif (ds2 == ds1): return True;
            else:
                if (ds2[s2[i]]>1): ds2[s2[i]] -= 1;
                else: del ds2[s2[i]];
                ds2[s2[j]] += 1;
                i += 1; j += 1;
        if (ds2 == ds1): return True;
        return False
            
            