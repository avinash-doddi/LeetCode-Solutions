from bisect import bisect_left as bs
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if (target in nums): return nums.index(target)
        else: return -1