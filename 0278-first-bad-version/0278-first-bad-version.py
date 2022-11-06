# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if (n == 1): return 1;
        start = 1; end = n; mid = (start + end)//2; val = 0; 
        while ((end - start) > 1):
            if (isBadVersion(mid)):
                end = mid; mid = (start + end)//2;
            else:
                start = mid; mid = (start + end)//2;
        if (isBadVersion(start)): return start
        return end            
                
                