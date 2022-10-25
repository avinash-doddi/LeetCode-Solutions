from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ds = deque(); n = 0; dt = deque(); m = 0;
        for i in s:
            if (n == 0):
                if (i == '#'): continue;
                else:
                    ds.append(i); n += 1;
            else:
                if (i == '#'):
                    ds.pop(); n -= 1;
                else:
                    ds.append(i); n += 1;
        for i in t:
            if (m == 0):
                if (i == '#'):continue;
                else:
                    dt.append(i); m += 1;
            else:
                if (i == '#'):
                    dt.pop(); m -= 1;
                else:
                    dt.append(i); m += 1;
        return ds == dt