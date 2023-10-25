
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        from collections import defaultdict as maps
        d = maps(int)
        temp = ""
        n = len(s)
        for i in range(n):
            temp = ""
            for letter in s[i]:
                temp += letter
                d[temp] += 1;
                
        temp = ""
        for a,b in d.items():
            if b == n:
                temp = max(temp, a);
        return temp
        