class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        while n > 1:
            tmp = []
            for i in range(n-1):
                tmp.append((nums[i]+nums[i+1])%10)
            nums = tmp; n -= 1;
        #print(nums)
        return nums[0]
