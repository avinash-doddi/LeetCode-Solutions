class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        def bfs(final, c, target, i, n, temp):
            if (i == n or target < 0): return
            if (target == 0):
                final.append(temp[:]); return
            temp.append(c[i]);
            bfs(final, c, target - c[i], i, n, temp)
            temp.pop()
            bfs(final, c, target, i+1, n, temp)
        n = len(c); temp = []; final = []
        bfs(final, c, target, 0, n, temp)
        return final