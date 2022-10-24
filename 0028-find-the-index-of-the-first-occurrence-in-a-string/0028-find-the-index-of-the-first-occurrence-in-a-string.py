class Solution:
    def strStr(self, h: str, n: str) -> int:
        if (n in h):
            return h.index(n)
        else: return -1;