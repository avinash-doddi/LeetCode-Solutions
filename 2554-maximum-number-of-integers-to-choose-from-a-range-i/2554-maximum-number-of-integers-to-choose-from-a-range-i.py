from collections import defaultdict as maps
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        d = maps(int);
        for i in banned: d[i] = 1;
        count = 0; summ = 0;
        for i in range(1,n+1):
            if d[i] == 0:
                if summ + i <= maxSum:
                    count += 1;
                    summ += i;
        return count
            