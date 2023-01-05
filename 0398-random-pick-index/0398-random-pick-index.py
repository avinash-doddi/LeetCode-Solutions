from collections import defaultdict as maps
from random import choice
class Solution:

    def __init__(self, nums: List[int]):
        self.d = maps(list); n = len(nums)
        for i in range(n):
            self.d[nums[i]].append(i);

    def pick(self, target: int) -> int:
        return choice(self.d[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)