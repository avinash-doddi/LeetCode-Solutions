import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter(s); n = len(s)
        for i in range(n): 
            if d[s[i]] == 1: return i;
        return -1