class Solution:
    def maxIceCream(self, cost: List[int], coins: int) -> int:
        cost.sort(); count = 0
        for i in cost:
            if (coins >= i):
                count += 1; coins -= i;
            else: break
        return count