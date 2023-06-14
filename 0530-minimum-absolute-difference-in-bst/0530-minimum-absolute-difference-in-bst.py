# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.arr = []; self.cnt = 0
        def traverse(root):
            if not root: return
            traverse(root.left)
            self.arr.append(root.val); self.cnt += 1;
            traverse(root.right);
        traverse(root); print(self.arr)
        if self.cnt <= 1: return 0
        minn = 1000000
        for i in range(self.cnt-1):
            minn = min(minn, abs(self.arr[i] - self.arr[i+1]))
        return minn