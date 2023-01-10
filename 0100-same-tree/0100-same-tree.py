# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # def inorder(root, arr):
        #     if root == None:
        #         arr.append(None); return
        #     inorder(root.left,arr);
        #     arr.append(root.val);
        #     inorder(root.right,arr);
        # parr = []; qarr = []
        # inorder(p, parr); inorder(q, qarr);
        # print(parr, qarr)
        # return parr == qarr
        if not p or not q: return p == q;
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val)