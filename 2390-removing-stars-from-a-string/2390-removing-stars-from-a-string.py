from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        d = deque();
        for i in s:
            if d and i == "*":
                d.pop();
            else: d.append(i)
        return "".join(d)