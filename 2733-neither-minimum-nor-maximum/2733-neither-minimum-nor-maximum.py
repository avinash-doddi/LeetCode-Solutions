class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        from collections import Counter as freq
        n = len(nums);
        if n == 1: return -1
        d = freq(nums);
        mx = max(nums); mn = min(nums)
        if d[mx] + d[mn] == n: return -1
        val = [i for i in nums if (i != mn and i != mx)]
        return val[0]