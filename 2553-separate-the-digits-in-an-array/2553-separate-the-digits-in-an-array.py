class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = [];
        nums = [str(i) for i in nums]
        for i in nums:
            for j in i:
                arr.append(int(j))
        return arr