class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        while len(s[-1]) < 1:
            s.pop()
        return len(s[-1])
        