from collections import defaultdict as maps
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeros = maps(int); conti = 0;
        for i in nums:
            if (i == 0):
                conti += 1;
            else:
                zeros[conti] += 1; conti = 0
        if (conti):
            zeros[conti] += 1; conti = 0;
        if (zeros):
            total = 0
            for x, y in zeros.items():
                total += ((x*(x+1))//2)*y
            return total
            
        return 0