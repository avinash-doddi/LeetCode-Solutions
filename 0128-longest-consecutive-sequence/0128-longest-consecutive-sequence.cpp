from sortedcontainers import SortedDict as maps
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxx = 0
        if (nums):
            d = maps()
            for i in nums:
                if (i in d):
                    d[i] += 1;
                else:
                    d[i] = 1;
            newarr = [x for x in d.keys()]; n = len(newarr); count = 1
            for i in range(1, n):
                if (abs(newarr[i] - newarr[i-1]) == 1): count += 1;
                else:
                    maxx = max(count, maxx); count = 1;
            maxx = max(count, maxx);
        return maxx
        