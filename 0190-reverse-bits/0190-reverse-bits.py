class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = ("0"*(32 - len(n)))+n;
        n = n[::-1]
        return int(n, 2)