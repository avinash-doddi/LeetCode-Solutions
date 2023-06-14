# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []; queue = [root]; n = 1;
        while(n > 0):
            temp = None; vec = []; cnt = 0; inp = 0
            for i in range(n):
                temp = queue.pop(0);
                #print(temp.val);
                vec.append(temp.val); inp += 1;
                if temp.right: 
                    queue.append(temp.right); cnt += 1;
                if temp.left: 
                    queue.append(temp.left); cnt += 1;
                
            n = cnt; ans.append(sum(vec)/inp); #print(vec, inp, sum(vec)/inp)
        return ans

