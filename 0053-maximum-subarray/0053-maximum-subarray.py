from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = -inf; summ = 0;
        for i in nums:
            summ += i;
            maxx = max(maxx, summ);
            summ = max(0, summ)
        return maxx