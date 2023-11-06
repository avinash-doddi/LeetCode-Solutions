class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter as freq
        x = freq(s);
        return "".join(sorted(s, reverse = True, key = lambda a: (x[a],a)))
    
        