from collections import defaultdict as maps
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        d = maps(int)
        for i in nums:
            d[i] += 1;
        maxlen = 0;
        for i in d.keys():
            l = 1; n = i*i;
            while True:
                if n in d:
                    l += 1; d[n] -= 1; n = n*n;
                else:
                    break;
            maxlen = max(maxlen, l);
        if maxlen >= 2: return maxlen
        return -1
        