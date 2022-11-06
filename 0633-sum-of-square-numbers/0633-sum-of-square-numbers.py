class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if (c <= 1): return True
        if (sqrt(c) == int(sqrt(c))): return True
        low = 1; high = int(sqrt(c));
        while(low <= high):
            fin = low*low + high*high;
            if (fin == c): return True
            if (fin < c):
                low += 1;
            if (fin > c): high -= 1;
        return False
        