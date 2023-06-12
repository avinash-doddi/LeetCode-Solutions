class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = sorted(set(nums), reverse = True)
        if len(s) > 2: return s[2]
        return s[0]