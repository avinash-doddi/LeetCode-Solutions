from collections import defaultdict as maps
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = maps(int);  x = 0; ans = 0;
        for i in range(len(s)):
            if d[s[i]]:
                x = max(x, d[s[i]]);
                d[s[i]] = 0
            d[s[i]] = i+1;
            ans = max(ans, i-x+1);
        return ans