class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        if (zeros > 1): return [0]*len(nums)
        product = 1; withoutzero = 1;
        for i in nums:
            if (i): withoutzero *= i;
            product *= i;
        for i in range(len(nums)):
            if (nums[i]): nums[i] = product // nums[i]
            else: nums[i] = withoutzero
        return nums