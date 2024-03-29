class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp
        res = [0] * (n+1)
        for i in range(1, n+1):
            res[i] = res[i//2] + (i&1)
        return res