# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def traverse(node, strs, tarr):
            if not node:
                return
            if node:
                tarr.append(chr(97 + node.val))
            if node.left == None and node.right == None:
                strs.append("".join(tarr)[::-1])
                tarr.pop(); return
            traverse(node.left, strs, tarr)
            traverse(node.right, strs, tarr)
            tarr.pop()
            
        strs,tarr,node = [],[],root
        traverse(node, strs, tarr)
        return min(strs)
        