from queue import PriorityQueue as pq
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        pqueue = pq(); n = len(arr);
        freq = Counter(arr);
        for value in freq.values():
            pqueue.put(n - value);
        half = n//2; count = 0;
        while(pqueue.qsize() > 0):
            if (half <= 0): return count;
            half -= (n - pqueue.get()); count += 1;
        return count
        