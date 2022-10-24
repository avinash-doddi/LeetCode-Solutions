class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxval = max(nums)
        return nums.index(maxval)