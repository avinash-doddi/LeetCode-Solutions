from collections import defaultdict as maps
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        ds = maps(int); n = len(s1)
        for i in range(n): 
            ds[s1[i]]+=1; ds[s2[i]]+=1;
        if (ds['x'] % 2 == 0 and ds['y'] % 2 == 0):
            xy = 0; yx = 0;
            for i in range(n):
                if (s1[i] == 'x' and s2[i] == 'y'):
                    xy += 1;
                if (s1[i] == 'y' and s2[i] == 'x'):
                    yx += 1;
            remxy = xy%2; remyx = yx%2;
            total = (xy//2)+(yx//2)+remxy+remyx;
            return total
        else:
            return -1
        