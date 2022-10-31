# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        new = []
        def preorder(root):
            if (root == None): return
            preorder(root.left);
            preorder(root.right);
            new.append(root.val);
        preorder(root);
        return new