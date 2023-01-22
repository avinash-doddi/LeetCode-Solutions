class Solution:
    def minOperations(self, a: List[int], b: List[int], k: int) -> int:
        high = []; low = []; n = len(a); h,l = 0,0; total = 0;
        for i in range(n):
            if k != 0:
                if abs(a[i] - b[i]) % k != 0: return -1;
                if a[i] != b[i]: 
                    total += (abs(a[i] - b[i]))//k;
                    if a[i] > b[i]:
                        high.append(a[i] - b[i]); h += 1;
                    if a[i] < b[i]:
                        low.append(b[i] - a[i]); l += 1;
            else:
                if a[i] != b[i]: return -1
        if total & 1 or h == n or l == n: return -1
        i = 0; j = 0; high.sort(); low.sort();
        while(i < h and j < l):
            if high[i] > low[j]:
                high[i] -= low[j]; low[j] = 0; j += 1;
            else:
                low[j] -= high[i]; high[i] = 0; i += 1;
        for i in high: 
            if i: return -1
        for j in low: 
            if j: return -1
        return total//2
        
        
                