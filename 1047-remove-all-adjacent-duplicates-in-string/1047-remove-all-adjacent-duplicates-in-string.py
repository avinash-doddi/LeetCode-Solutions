from collections import deque
class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s);
        if (n == 1): return s;
        d = deque(); d.append(s[0]); count = 1;
        for i in range(1, n):
            if (count > 0): 
                x = d.pop(); count -= 1;
                if (x != s[i]):
                    d.append(x); d.append(s[i]); count += 2;
            else:
                d.append(s[i]); count += 1;
        finalstr = "".join(d)
        return finalstr
                