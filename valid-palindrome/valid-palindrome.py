class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower();
        news = ''
        for i in s:
            if 'a' <= i <= 'z' or '0' <= i <= '9':
                news += i;
        return news == news[::-1]
                