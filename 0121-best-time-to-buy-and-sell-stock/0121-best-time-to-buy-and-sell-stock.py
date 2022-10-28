from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices);  maxprofit = 0;
        if (n > 0):
            prefix = [0]*n; temp = 0
            for i in range(n-1, -1, -1):
                temp = max(temp, prices[i]);
                prefix[i] = temp;
                
            for i in range(n):
                maxprofit = max(maxprofit, prefix[i]-prices[i]);
        return maxprofit