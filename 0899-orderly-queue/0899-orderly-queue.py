class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        def K_is_1(s):
            n = len(s); final = s;
            for i in range(n):
                s = (s[1:n] + s[0]);
                final = min(s, final);
            return final
        if (k == 1): return K_is_1(s);
        s = [char for char in s];
        s.sort();
        return "".join(s);