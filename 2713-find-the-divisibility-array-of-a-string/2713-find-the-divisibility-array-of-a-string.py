class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        temp = 0; ans = []
        for i in word:
            temp = (temp*10 + int(i))
            if temp % m == 0: ans.append(1)
            else: ans.append(0)
            temp %= m;
        return ans