class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if (n == 1): return []
        else:
            frac = set()
            for i in range(1,n):
                for j in range(2, n+1):
                    g = gcd(i,j);
                    k = i//g; kk = j//g;
                    if (k < kk):
                        frac.add(str(k)+'/'+str(kk))
            return list(frac)