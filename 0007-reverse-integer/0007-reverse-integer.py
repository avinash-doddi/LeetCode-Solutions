class Solution:
    def reverse(self, x: int) -> int:
        mod = 2**31 - 1; neg = -(2**31);
        v =  x; x = str(x);
        if (v < 0):
            x = (x[1:])[::-1];
            x = -(int(x));
            if (neg > x): return 0;
            else: return x;
        else:
            x = int(x[::-1])
            if (x > mod): return 0;
            else: return x