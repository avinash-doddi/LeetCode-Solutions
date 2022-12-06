class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def bfs(init, final, temp, target, k, i, n):
            if (k == 0):
                if (target == 0): 
                    final.append(temp[:]); return
                else: return
            if (i == n or target < 0): return
            temp.append(init[i]);
            bfs(init, final, temp, target-init[i], k-1, i+1, n)
            temp.pop()
            bfs(init, final, temp, target, k, i+1, n)
        
        init = [i for i in range(1,10)]
        final = []; temp = []
        bfs(init, final, temp, n, k, 0, 9)
        return final