class Solution:
    
    def reverseVowels(self, s: str) -> str:
        def isvowel(i):
            return i in 'aeiouAEIOU'
        
        s = [i for i in s];
        vowel = [i for i in s if isvowel(i)];
        vowel.reverse(); j = 0;
        for i in range(len(s)):
            if (isvowel(s[i])):
                s[i] = vowel[j]; j += 1;
        return "".join(s)