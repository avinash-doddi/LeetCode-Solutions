from queue import PriorityQueue as pq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        pqueue = pq();
        for i in nums: pqueue.put(i);
        del nums; nums = []
        while(pqueue.qsize() > 0):
            nums.append(pqueue.get())
        return nums