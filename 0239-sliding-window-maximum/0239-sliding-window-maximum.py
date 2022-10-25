from sortedcontainers import SortedList as slist
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if (k == 1): return nums;
        finarr = []; i = 0; j = 0; n = len(nums); d = slist();
        while(j < n):
            if (j < k):
                d.add(nums[j]); j += 1;
            else:
                finarr.append(d[-1]);
                d.remove(nums[i]); d.add(nums[j]);
                i += 1; j += 1;
        finarr.append(d[-1]);
        return finarr
            
        
        
            