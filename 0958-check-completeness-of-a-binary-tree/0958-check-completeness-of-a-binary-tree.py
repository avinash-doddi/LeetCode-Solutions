# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if (root == None): return root;
        queue = [root]; n = 1; flag = 0
        while (n):
            temp = None;
            for i in range(n):
                temp = queue.pop(0);
                if (temp == None): flag = 1;
                else:
                    if (flag): return False
                    queue.append(temp.left);
                    queue.append(temp.right);
            n = len(queue)
        return True