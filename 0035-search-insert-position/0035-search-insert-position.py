class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0; last = len(nums) - 1; mid = (start + last)//2;
        if (nums[mid] == target): return mid;
        while (start <= last):
            mid = (start + last)//2;
            if (nums[mid] == target): return mid
            if (nums[mid] < target):
                start = mid + 1;
            if (nums[mid] > target):
                last = mid - 1;
        return start