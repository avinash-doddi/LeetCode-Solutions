from collections import Counter as freq
class Solution:
    def frequencySort(self, s: str) -> str:
        d = freq(s); s = list({i for i in s})
        s.sort(key =  lambda i: d[i], reverse = True)
        ans = ''; 
        for i in s: ans += i*d[i]
        return ans