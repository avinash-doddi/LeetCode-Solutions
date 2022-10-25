class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        
        if max(arr) < 0: return max(arr);
        
        currmax = maxsum = currmin = minsum = arr[0]; length = len(arr);
        for i in range(1, length):
            currmax = max(currmax + arr[i], arr[i])
            maxsum = max(maxsum, currmax);
            currmin = min(currmin + arr[i], arr[i])
            minsum = min(minsum, currmin);
        return max(maxsum, sum(arr) - minsum)