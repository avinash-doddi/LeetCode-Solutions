class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        subarr, cnt = [], 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                cnt += 1;
            else:
                if cnt: 
                    subarr.append(cnt+1); cnt = 0
                else: subarr.append(1)
        if cnt: subarr.append(cnt + 1)
        else: subarr.append(1);
        total = 0
        #print(subarr)
        for i in subarr:
            total += ((i*(i+1))//2)
        return total
        