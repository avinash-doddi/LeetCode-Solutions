from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums); n = len(nums)//3; fin = []
        for x, y in d.items():
            if (y > n): fin.append(x)
        return fin