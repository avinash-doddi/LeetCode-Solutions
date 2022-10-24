class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        val = abs(dividend)//abs(divisor)  
        if dividend < 0 and divisor < 0: pass;
        elif (dividend < 0 or divisor < 0): 
            val = -val;
            
        if (val < -2**31): return 2**31
        if (val > 2**31 - 1): return 2**31 - 1;
        return val