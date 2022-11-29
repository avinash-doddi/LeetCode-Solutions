from collections import defaultdict as maps
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = maps(int); n = len(names)
        for i in range(n):
            if (d[names[i]]):
                val = names[i] + "(" + str(d[names[i]]) + ")"
                while val in d:
                    d[names[i]] += 1;
                    val = names[i] + "(" + str(d[names[i]]) + ")"
                d[val] += 1; names[i] = val;
            else:
                d[names[i]] += 1;
        return names