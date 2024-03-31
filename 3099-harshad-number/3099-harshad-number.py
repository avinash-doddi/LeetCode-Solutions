class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x = str(x)
        sm = 0
        for i in x:
            sm += int(i)
        if int(x) % sm == 0: return sm
        return -1
        