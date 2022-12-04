class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = title.split(" ")
        for i in range(len(s)):
            if (len(s[i]) <= 2): s[i] = s[i].lower()
            else: s[i] = s[i].title()
        return " ".join(s)