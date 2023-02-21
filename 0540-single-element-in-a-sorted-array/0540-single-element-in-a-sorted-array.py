class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        c = 0
        for i in nums: c ^= i;
        return c