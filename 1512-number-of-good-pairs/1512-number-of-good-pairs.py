class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        d = Counter(nums); total = 0
        return sum([(d[i]*(d[i]-1)//2) for i in d])
        