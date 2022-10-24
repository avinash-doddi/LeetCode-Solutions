class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num % 3 != 0): return []
        ref = num//3;
        arr = [ref - 1, ref, ref + 1]
        return arr