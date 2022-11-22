class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def recur(arr, target, i, n, fin, temp):
            if (target == 0):
                fin.append(temp[:]); return;
            if (i >= n or target < 0): return;
            temp.append(arr[i]);
            recur(arr, target-arr[i], i+1, n, fin, temp);
            temp.pop();
            while i+1 < n and arr[i] == arr[i+1]:
                i += 1;
            recur(arr, target, i+1, n, fin, temp);
        fin = []; temp = []; i = 0; n = len(candidates);
        candidates.sort(); fin = []
        recur(candidates, target, i, n, fin, temp);
        return fin;
            