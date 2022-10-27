class Solution:
    def countOdds(self, low: int, high: int) -> int:
        val = 0;
        if (low & 1 and high & 1):
            val = 2;
            val += (high - low)//2 - 1;
        elif (low & 1 or high & 1):
            val = 1;
            val += (high - low)//2;
        else:
            val = (high - low)//2;
        return val;