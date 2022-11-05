class Solution:
    def arrangeWords(self, text: str) -> str:
        string = text.split()
        string.sort(key = len)
        string = " ".join(string)
        return string.capitalize()