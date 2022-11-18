class Solution:
    
    def recur(self, candidates, i, n, target):
        if (target == 0):
            self.arr.append(self.ref[:]); 
            return;
        if (i >= n or target < 0): return;
        self.ref.append(candidates[i]);
        self.recur(candidates, i, n, target-candidates[i]);
        self.ref.pop();
        self.recur(candidates, i+1, n, target);
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.arr = []; self.ref = []; n = len(candidates);
        self.recur(candidates, 0, n, target);
        return self.arr