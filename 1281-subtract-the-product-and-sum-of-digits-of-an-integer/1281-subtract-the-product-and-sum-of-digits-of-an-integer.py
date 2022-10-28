class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = sum([int(x) for x in str(n)]); pro = 1
        for i in str(n):
            pro *= int(i)
        return pro-summ