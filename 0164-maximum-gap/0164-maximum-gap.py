class Solution:
    def maximumGap(self, arr: List[int]) -> int:
        arr.sort()
        maxx = 0; n = len(arr)
        for i in range(n-1):
            maxx = max(maxx, arr[i+1] - arr[i])
        return maxx