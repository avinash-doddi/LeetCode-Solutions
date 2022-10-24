# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        returnarr = []
        if (root):
            queue = [root]; n = len(queue)
            while(n > 0):
                temp = None; vector = []; v = 0;
                for i in range(n):
                    temp = queue.pop(0);
                    vector.append(temp.val);
                    if (temp.left): queue.append(temp.left);
                    if (temp.right): queue.append(temp.right);
                returnarr.append(vector[-1]); del vector;
                n = len(queue);
                                                                   
        return returnarr