from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = maxx = nums[0]; n = len(nums)
        for i in range(1,n):
            curr = max(curr+nums[i], nums[i])
            maxx = max(curr, maxx)
        return maxx