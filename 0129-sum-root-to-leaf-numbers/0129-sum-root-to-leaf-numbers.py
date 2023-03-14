# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(root, arr, summ):
            if root == None:
                return
            arr.append(str(root.val));
            if root.left == None and root.right == None:
                summ += int("".join(arr));
                arr.pop(); self.sm.append(summ); return 
            traverse(root.left, arr, summ); 
            traverse(root.right, arr, summ);
            arr.pop()
        arr = []; summ = 0; self.sm = []
        traverse(root, arr, summ)
        return sum(self.sm)
            
            