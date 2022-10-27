from collections import defaultdict as maps
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        final = ''; d = maps(int);
        for i in s: d[i] += 1;
        for i in order:
            final += (i*d[i]); del d[i];
        remaining = []
        for i in d.keys():
            while(d[i]):
                remaining.append(i); d[i] -= 1;
        remaining.sort();
        return final + "".join(remaining)