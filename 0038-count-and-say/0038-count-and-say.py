from collections import defaultdict as mp
class Solution:
    def countAndSay(self, n: int) -> str:
        d = mp(int);
        arr = [0, '1'];
        if (n == 1): return "1";a
        for i in range(2, n+1):
            val = arr[i-1]; m = len(val); fin = ''; prev = '';
            for j in range(m):
                if (j == 0):
                    d[val[j]] += 1; prev = val[j];
                else:
                    if (val[j] == prev):
                        d[val[j]] += 1;
                    else:
                        fin += (str(d[prev])) + prev;
                        del d[prev]; d[val[j]] += 1; prev = val[j];
            if (prev in d): 
                fin += (str(d[prev])) + prev; del d[prev];
            arr.append(fin);
        return arr[-1]
                