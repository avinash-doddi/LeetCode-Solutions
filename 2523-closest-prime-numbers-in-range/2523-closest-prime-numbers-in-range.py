class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [1]*(right + 1)
        def primes(n, prime):
            prime[0], prime[1] = 0,0; i = 2;
            while(i*i <= n):
                for j in range(i*i, n, i):
                    if prime[j] : prime[j] = 0;
                i += 1;
        primes(right + 1, prime);
        minn = 1000000; prev = -1; num1 = 0; num2 = 0
        for i in range(left, right+1):
            if prime[i]:
                if prev == -1:
                    prev = i;
                else:
                    if i - prev < minn:
                        minn = i - prev;
                        num1 = prev; num2 = i;
                    prev = i;
        if num1 and num2: return [num1, num2]
        return [-1,-1]
                
        
        
        