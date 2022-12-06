class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def dfs(final, s, i, n):
            if (i >= n):
                final.append("".join(s)); return
            if (97 <= ord(s[i]) <= 122):
                s[i] = s[i].upper()
                dfs(final, s, i+1, n)
                s[i] = s[i].lower()
            if (65 <= ord(s[i]) <= 90):
                s[i] = s[i].lower()
                dfs(final, s, i+1, n)
                s[i] = s[i].upper()
            dfs(final, s, i+1, n)
        
        s = [i for i in s]; final = []
        dfs(final, s, 0, len(s))
        return final
        