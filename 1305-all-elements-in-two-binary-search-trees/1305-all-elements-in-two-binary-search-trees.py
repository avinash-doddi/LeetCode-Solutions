# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lst):
        if (root == None): return
        
        self.solve(root.left, lst);
        lst.append(root.val);
        self.solve(root.right,lst);
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        finallist = [];
        self.solve(root1, finallist);
        self.solve(root2, finallist);
        finallist.sort();
        return finallist
 

            