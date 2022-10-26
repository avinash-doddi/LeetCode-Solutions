from collections import defaultdict as maps
class Solution:
    def canConstruct(self, ransom: str, magazine: str) -> bool:
        d = maps(int)
        for i in magazine: d[i] += 1;
        for i in ransom:
            if (d[i]): d[i] -= 1;
            else: return False
        return True