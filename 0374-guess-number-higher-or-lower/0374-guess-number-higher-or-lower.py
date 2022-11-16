# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1; end = n; mid = start + (end - start)//2;
        if (guess(start) == 0): return start;
        if (guess(end) == 0): return end;
        if (guess(mid) == 0): return mid;
        while(start <= end):
            if (guess(mid) ==0): return mid;
            if (guess(mid) == -1):
                end = mid-1; mid = start + (end - start)//2;
            elif (guess(mid) == 1):
                start = mid+1; mid = start + (end - start)//2;