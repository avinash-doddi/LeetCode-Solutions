from math import inf
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0; prev = -inf; intervals.sort()
        for i in intervals:
            if i[0] >= prev:
                prev = i[1];
            else:
                count += 1;
                prev = min(prev, i[1]);
        return count