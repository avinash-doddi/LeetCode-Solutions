from queue import deque
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        sm = sum(arr[:k]); cnt = 0; n = len(arr)
        if sm/k >= t: cnt += 1;
        for i in range(k,n):
            sm = sm + arr[i] - arr[i-k];
            if sm/k >= t: 
                #print(arr[i-k+1: i+1])
                cnt += 1
        return cnt
        