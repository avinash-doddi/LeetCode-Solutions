class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        count = 1; n = len(s); maxcount = 0; i = 1;
        while(i < n):
            if (ord(s[i-1]) < ord(s[i]) and abs(ord(s[i-1]) - ord(s[i])) == 1):
                count += 1;
            else:
                maxcount = max(count, maxcount); count = 1;
            i += 1;
        maxcount = max(count, maxcount);
        return maxcount
                