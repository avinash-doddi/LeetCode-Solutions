class Solution:
    def findMin(self, nums: List[int]) -> int:
        high = len(nums)-1; low = 0;
        mid = 0;
        while(low < high):
            
            mid = (low + (high - low)//2);
            
            if (nums[high] > nums[mid]):
                high = mid;
            elif (nums[high] < nums[mid]):
                low = mid + 1;
            else:
                high -= 1;
                
        return nums[low]
    
    