class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s); count = 0
        for i in range(n):
            ref = ''
            for j in range(i, n):
                ref += s[j];
                if (ref == ref[::-1]): count += 1;
        return count