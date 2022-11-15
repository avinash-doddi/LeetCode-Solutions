from itertools import permutations as per
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [str(i) for i in range(1, n+1)]
        if (k == 1): return "".join(arr);
        j = 0; perr = per(arr);
        #for i in perr: print(i)
        for i in perr:
            j += 1;
            if (j == k): 
                return "".join(i);
            