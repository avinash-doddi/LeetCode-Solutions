from itertools import permutations 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = permutations(nums)
        finalperm = []
        for perm in permutation:
            finalperm.append(perm)
        return finalperm