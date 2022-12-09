# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    maxx = -inf; size = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def preorder(root):
            if root == None: return
            arr.append(root.val); self.size += 1;
            if (not root.left and not root.right):
                for i in range(self.size):
                    for j in range(i+1, self.size):
                        self.maxx = max(self.maxx, abs(arr[i]-arr[j]))
            preorder(root.left)
            preorder(root.right)
            arr.pop(); self.size -= 1;
            
        arr = []; preorder(root)
        return self.maxx