from collections import defaultdict as maps
class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        d = maps(int)
        for i in a: d[i] += 1;
        newarr = []
        for i in b:
            if (d[i]):
                newarr.append(i); d[i] -= 1;
        return newarr