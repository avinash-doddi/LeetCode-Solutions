from math import inf
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort();
        ii = intervals[0][0]; prev = intervals[0][1]; newintervals = []
        del intervals[0];
        for i in intervals:
            if i[0] <= prev:
                prev = max(prev, i[1]);
            else:
                newintervals.append([ii, prev]);
                ii = i[0]; prev = i[1];
        newintervals.append([ii, prev]);
        return newintervals
        
        