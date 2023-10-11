class Solution:
    def minOperations(self, nums: List[int]) -> int:
        original = len(nums); minoper = original;
        nums = sorted(set(nums)); new = len(nums);
        right = 0
        for left in range(new):
            while right < new and nums[right] < nums[left] + original:
                right += 1;
            minoper = min(minoper, original - (right - left))
        return minoper
        
        
        