class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        cnt, total = 0, 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                cnt += 1;
            else:
                if cnt: 
                    total += ((cnt+1) * (cnt+2))//2;  cnt = 0
                else: total += 1;
        if cnt: total += ((cnt+1) * (cnt+2))//2
        else: total += 1
        return total
        