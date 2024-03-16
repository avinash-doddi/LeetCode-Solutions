class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict as maps, deque as dq
        initSum = sum(nums)
        n = len(nums)
        chkPresence = maps(int)  # initially for indices to sort deque
        for i in range(n):
            chkPresence[i] = nums[i];
        new_nums = sorted(chkPresence.keys(), key  = lambda x : (chkPresence[x],x ))
        keepTrack = dq(new_nums); del new_nums
        #now chkPresence is for checking whether any element in marked or not.
        
        finArr = []   # result after each query..
        
        for indx, cnt in queries:
            
            # if unMarked::
            if chkPresence[indx] != -1:
                chkPresence[indx] = -1;
                initSum -= nums[indx]
            
            while cnt > 0 and n > 0:
                indx = keepTrack.popleft()
                n -= 1;
                if chkPresence[indx] != -1:
                    chkPresence[indx] = -1
                    initSum -= nums[indx]
                    cnt -= 1;
                        
            finArr.append(initSum)
        
        return finArr 