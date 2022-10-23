from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = Counter(nums); n = len(nums);
        fakeval = [x for x,y in d.items() if y == 2]
        remval = [i for i in range(1, n+1) if i not in d]
        return fakeval+remval