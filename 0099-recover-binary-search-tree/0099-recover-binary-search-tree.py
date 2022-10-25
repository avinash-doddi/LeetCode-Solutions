# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def retrieve(self, root):
        if (root == None): return
        self.retrieve(root.left);
        self.lst.append(root.val);
        self.retrieve(root.right);
    
    def assign(self, root):
        if (root == None): return;
        self.assign(root.left);
        root.val = self.lst.pop(0);
        self.assign(root.right);
        
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.lst = []
        self.retrieve(root);
        self.lst.sort();
        self.assign(root);