from collections import defaultdict as maps
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(); d = maps(str); freq = maps(int)
        n = len(s); m = len(pattern)
        if n != m: return False
        for i in range(n):
            if d[s[i]]:
                if d[s[i]] != pattern[i]:
                    return False
            else:
                if freq[pattern[i]]: return False
                d[s[i]] = pattern[i]; freq[pattern[i]] = 1;
                
        return True