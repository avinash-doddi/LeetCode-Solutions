from queue import PriorityQueue as pq
from math import ceil
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        d = pq(); ref = 10000000000
        for i in nums: d.put(ref - i);
        total = 0;
        while (k > 0):
            val = ref - d.get(); total += val;
            d.put(ref - int(ceil(val/3))); k -= 1;
        return total
            