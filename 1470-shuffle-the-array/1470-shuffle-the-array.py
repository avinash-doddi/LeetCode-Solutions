class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(chain(*zip(nums[:n],nums[n:])))  