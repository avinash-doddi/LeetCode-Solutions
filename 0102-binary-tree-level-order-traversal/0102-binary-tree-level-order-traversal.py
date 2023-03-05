# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.returnarr = []
        if (root == None): return []
        queue = [root]; n = len(queue)
        while(n):
            temp = None; vector = []
            for i in range(n):
                temp = queue.pop(0); vector.append(temp.val);
                if (temp.left): queue.append(temp.left);
                if (temp.right): queue.append(temp.right);
            self.returnarr.append(vector); del vector; n = len(queue);
        return self.returnarr