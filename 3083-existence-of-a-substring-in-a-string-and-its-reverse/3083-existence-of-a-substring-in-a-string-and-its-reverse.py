class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)  
        if n == 1: return False
        if n == 2: 
            return s == s[::-1]  
        rev = s[::-1]
        for i in range(n-1):
            if s[i]+s[i+1] in rev: return True
        return False
