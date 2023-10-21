class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s); r = 0; m = 0; fin = ''
        if s == s[::-1]: return s
        for i in range(n):
            ref = ''; r = 0;
            for j in range(i, n):
                ref += s[j]; r += 1;
                if (ref == ref[::-1]):
                    if (r > m):
                        m = r; fin = ref;
        return fin
                