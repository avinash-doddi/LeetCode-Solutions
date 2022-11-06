from queue import PriorityQueue as pq
from collections import defaultdict as maps
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = maps(list); pqueue = pq();
        for x, y in points:
            hypo = (x**2)+(y**2);
            d[hypo].append([x,y]);
            pqueue.put(hypo);
        final_points = []
        while (k > 0):
            key = pqueue.get();
            final_points.append(d[key][0]); 
            del d[key][0]; k -= 1;
        return final_points