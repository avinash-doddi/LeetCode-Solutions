from collections import deque
class Solution:
    def makeGood(self, s: str) -> str:
        stack = deque(); n = len(s)
        for i in range(n):
            if (stack):
                if abs(ord(stack[-1]) - ord(s[i])) == 32:
                    stack.pop();
                else: stack.append(s[i]);
            else:
                stack.append(s[i]);
        return "".join(stack)