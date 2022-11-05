from queue import PriorityQueue as pq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        pqueue = pq(); temp = 10000000;
        initial_sum = sum(nums);
        half = initial_sum/2;
        for i in nums: 
            pqueue.put(temp - i);  # to get a priority Queue where elements are ordered in decreasing order ;)
        oper = 0;
        while (pqueue.qsize() > 0):
            number = temp - pqueue.get();
            initial_sum -= number;
            number = number/2; oper += 1;
            initial_sum += number;
            if (initial_sum <= half): return oper
            pqueue.put(temp - number);
        return oper;
            

        