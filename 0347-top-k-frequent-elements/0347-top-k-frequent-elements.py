from collections import Counter
from queue import PriorityQueue as pq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums); n = len(nums);
        pqueue = pq();
        for key, value in freq.items():
            pqueue.put([n-value, key]) 
        returnarr = []
        while (k > 0):
            returnarr.append(pqueue.get()[1]); k -= 1;
        return returnarr;
            