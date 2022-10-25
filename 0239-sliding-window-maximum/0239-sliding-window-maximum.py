# O(N LogN) method
from sortedcontainers import SortedList as slist
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if (k == 1): return nums;
        finarr = []; d = slist();
		i = 0; j = 0; n = len(nums); 
        while(j < n):
            if (j < k):
                d.add(nums[j]); j += 1;
            else:
                finarr.append(d[-1]);
                d.remove(nums[i]); d.add(nums[j]); # fixed K size
                i += 1; j += 1;
        finarr.append(d[-1]);  #since last iteration is left
        return finarr 




#**Optimized Code** O(N)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque(); result = []
        for i, current in enumerate(nums):
            while d and nums[d[-1]] <= current:
                d.pop();
            d.append(i);
            if d[0] == i-k:
                d.popleft();
            if i >= k-1:
                result.append(nums[d[0]]);
        return result
