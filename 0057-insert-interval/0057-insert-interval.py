class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval);
        intervals.sort(); newinter = []
        prev = intervals[0][1]; ii = intervals[0][0];
        del intervals[0];
        for i in intervals:
            if i[0] <= prev:
                prev = max(prev, i[1]);
            else:
                newinter.append([ii, prev]);
                ii = i[0]; prev = i[1];
        newinter.append([ii, prev]);
        return newinter