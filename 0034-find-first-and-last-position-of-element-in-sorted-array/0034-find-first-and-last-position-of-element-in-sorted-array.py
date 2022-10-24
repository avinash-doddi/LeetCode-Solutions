from bisect import bisect_left, bisect_right;
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums); ret = []; c = 0;
        if (n == 0): return [-1,-1]
        in1 = bisect_left(nums, target, 0, n);
        in2 = bisect_right(nums, target, 0, n);
        if (in1 < n):
            if (nums[in1] == target): 
                ret.append(in1); c += 1; in1 = -1;
            if (in2 != 0):
                if (nums[in2-1] == target):
                    ret.append(in2-1); c += 1; in2 = -1;
        if (in1 != -1):
            return [-1,-1]
        return ret
            
        