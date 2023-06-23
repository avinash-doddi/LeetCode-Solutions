class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        a,e,i,o,u = 0,0,0,0,0; n = len(word); j = 0; ans = 0
        while j < n:
            while j < n and word[j] == 'a': 
                a += 1; j += 1;
            while j < n and word[j] == 'e': 
                e += 1; j += 1;
            while j < n and word[j] == 'i': 
                i += 1; j += 1;
            while j < n and word[j] == 'o': 
                o += 1; j += 1;
            while j < n and word[j] == 'u': 
                u += 1; j += 1;
            if a and e and i and o and u: ans = max(ans, a+e+i+o+u)
            a,e,i,o,u = 0,0,0,0,0;
        return ans