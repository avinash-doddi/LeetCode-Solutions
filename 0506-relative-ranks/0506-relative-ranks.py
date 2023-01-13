from queue import PriorityQueue as pq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pqueue = pq(); ref = 10000000;
        d = {i:0 for i in score};
        for i in score:
            pqueue.put(ref - i);
        rank = 1; n = len(score);
        for i in range(n):
            temp = ref - pqueue.get();
            if rank == 1:
                d[temp] = 'Gold Medal';
            elif rank == 2:
                d[temp] = 'Silver Medal'
            elif rank == 3:
                d[temp] = 'Bronze Medal';
            else:
                d[temp] = str(rank);
            rank += 1;
        for i in range(n):
            score[i] = d[score[i]];
        return score
        