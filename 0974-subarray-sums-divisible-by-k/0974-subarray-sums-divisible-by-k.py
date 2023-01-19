class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        rems = {0:1}; sum = 0; total = 0; r = 0;
        for i in range(n):
            sum += nums[i];
            r = sum % k;
            if r not in rems: rems[r] = 0 
            total += rems[r];
            rems[r] += 1;
        return total