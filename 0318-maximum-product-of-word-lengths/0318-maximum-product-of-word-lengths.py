class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def common(word1, word2):
            for w1, w2 in zip(word1, word2):
                if w1 and w2: return True
            return False
            
        chars, ans = [[False]*26 for i in range(len(words))], 0;
        for index, word in enumerate(words):
            for char in word:
                chars[index][ord(char) - ord('a')] = True;
            for j in range(index):
                if not common(chars[index], chars[j]):
                    ans = max(ans, len(words[index])*len(words[j]))
        return ans