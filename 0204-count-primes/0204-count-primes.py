class Solution:          
    def countPrimes(self, n: int) -> int:
        if (n < 3): return 0;
        seive = [1]*n;
        seive[0] = seive[1] = 0; i = 2
        while(i*i < n):
            if (seive[i]):
                seive[i*i:n:i] = [0]*(1 + (n - i*i - 1)//i)
            i += 1 if (i == 2) else 2
        return sum(seive)