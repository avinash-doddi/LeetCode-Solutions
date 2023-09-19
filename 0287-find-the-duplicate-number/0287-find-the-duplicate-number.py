from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums);
        for x,y in freq.items():
            if (y > 1): 
                return x;