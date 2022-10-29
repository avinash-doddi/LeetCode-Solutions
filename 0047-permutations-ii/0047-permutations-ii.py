from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        generated_perms = permutations(nums)
        #now remove duplicates
        sett = set(generated_perms)
        return list(sett)