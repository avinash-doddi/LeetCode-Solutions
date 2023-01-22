class Solution:
    def minOperations(self, a: List[int], b: List[int], k: int) -> int:
        high = 0; low = 0; n = len(a);total = 0;
        for i in range(n):
            if k != 0:
                if abs(a[i] - b[i]) % k != 0: return -1;
                if a[i] != b[i]: 
                    total += (abs(a[i] - b[i]))//k;
                    if a[i] > b[i]:
                        high += (a[i] - b[i]); 
                    if a[i] < b[i]:
                        low += (b[i] - a[i]);
            else:
                if a[i] != b[i]: return -1
        if total & 1: return -1
        if abs(low - high) != 0: return -1
        return total//2
        
        
                