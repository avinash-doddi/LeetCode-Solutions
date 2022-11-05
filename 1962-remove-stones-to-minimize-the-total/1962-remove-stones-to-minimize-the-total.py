from queue import PriorityQueue as pq
from math import ceil
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pqueue = pq(); temp = 1000000;
        for i in piles: 
            pqueue.put(temp - i);  # to get a priority Queue where elements are ordered in decreasing order ;)
        while (k > 0):
            number = temp - pqueue.get(); #retreiving number
            number = ceil(number / 2);
            pqueue.put(temp - number); k -= 1;
        total = 0;
        while(pqueue.qsize() > 0):
            total += (temp - pqueue.get())
        return total
        