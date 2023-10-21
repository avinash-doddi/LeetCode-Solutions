class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_left_right(l,r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1; r += 1;
            return s[l+1:r]
        """
        we take a particular index and check if left and right of it are equal
        and we go on like that till they are not equal.
        complexity: O(n^2)
        """
        n = len(s)
        res = ""
        for i in range(n):
            sub1 = check_left_right(i,i)
            if len(sub1) > len(res):
                res = sub1;
            sub1 = check_left_right(i,i+1) # for cases like "cbbd" => "bb"
            if len(sub1) > len(res):
                res = sub1;
        return res
                
        