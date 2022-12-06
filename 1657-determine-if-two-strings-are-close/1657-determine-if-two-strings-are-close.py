from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def data(string):
            freq = Counter(string)
            letters = sorted(freq.keys())
            values = sorted(freq.values())
            return (letters, values)
        return data(word1) == data(word2)