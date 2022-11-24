from math import gcd
class Solution:
    def minOperations(self, nums: List[int], numDiv: List[int]) -> int:
        nums.sort(); numDiv.sort();
        totalgcd = numDiv[0];
        for i in numDiv:
            totalgcd = gcd(totalgcd, i);
        if (nums[0] > totalgcd):
            return -1;
        count = 0;
        for i in nums:
            if (totalgcd % i == 0):
                return count
            count += 1;
        return -1