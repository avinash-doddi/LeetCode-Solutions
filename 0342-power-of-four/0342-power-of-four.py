class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n <= 0): return 0;
        if (n == 1): return 1;
        if (n & 1): return 0;
        count = 0; itr = 0
        while(n > 0):
            itr += 1;
            if (n & 1): count += 1;
            n >>= 1;
        val = itr - count;
        print(val, itr, count)
        if (val % 2 == 0 and count == 1): return 1;
        else: return 0;