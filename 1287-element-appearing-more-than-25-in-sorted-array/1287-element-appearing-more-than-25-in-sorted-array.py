class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from bisect import bisect_left as lwr, bisect as upr
        n = len(arr)
        for i in [arr[n//4], arr[n//2], arr[3*n//4], arr[n-1]]:
            lb = lwr(arr, i)
            ub = upr(arr, i)
            if ub - lb > n//4:
                return i;
        return -1
