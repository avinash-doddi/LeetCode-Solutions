class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda x: (bin(x).count('1'),len(bin(x)), x))
        return arr